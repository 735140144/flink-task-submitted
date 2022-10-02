"""
@function:
@parameter:
@attention:
"""
import os
from typing import Union
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel
import flinkcommitconf as conf
import hdfsupload


class Params(BaseModel):
    namespace: str = conf.NAMESPACE
    jarpath: str = conf.LOCAL_PATH
    jar: str = None
    classentry: str = None
    appname: str = None
    ckname: str = None
    model: str = None
    fromck: str = None
    taskprocess: str = None
    taskmem: str = None
    slotnum: str = None
    jbheap: str = None
    jboffheap: str = None
    dwonpath: str = None


app = FastAPI()


def reponse(*, code=200, data: Union[list, dict, str], message="Success") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': code,
            'message': message,
            'data': data,
        }
    )


@app.post('/flink')
async def start_flink(params: Params):
    # 验证模式
    if params.model == "yarn":
        try:
            os.system("/opt/cloudera/parcels/FLINK-1.13.6-BIN-SCALA_2.11/lib/flink/bin/yarn-session.sh -d -nm "
                      "Flink-session -Djobmanager.memory.process.size=4096mb -Djobmanager.memory.jvm-metaspace.size=2048m")
        except:
            return reponse(code=300, data={'detail': "yarn启动失败"}, message="failed")
        finally:
            return reponse(data={'detail': "yarn启动成功"})
    elif params.model == "yarn-session":
        command = "flink run -d "
    elif params.model == "yarn-per-job":
        command = "flink run -t yarn-per-job -d "
    else:
        return reponse(code=301, data={'detail': "model参数异常"}, message="failed")

    if params.fromck == "yes":
        try:
            strip = os.popen(
                "hdfs dfs -ls /flink-checkpoints/" + params.ckname + "/* |sort -r -k6,7 | grep chk |head -1 | awk '{print $8}'").readline().strip(
                '\n')
            if strip != None or strip != '':
                command = command + "-s hdfs://" + params.namespace + strip
        except:
            return reponse(code=302, data={'detail': "获取checkpoint目录异常"}, message="failed")

    if params.model == "yarn-per-job":
        # 参数
        command = command + " -Dyarn.application.name=" + params.appname

        if params.taskprocess is not None:
            command = command + " -Dtaskmanager.memory.process.size=" + params.taskprocess

        if params.taskmem is not None:
            command = command + " -Dtaskmanager.memory.managed.size=" + params.taskmem

        if params.slotnum is not None:
            command = command + " -Dtaskmanager.numberOfTaskSlots=" + params.slotnum

        if params.jbheap is not None:
            command = command + " jobmanager.memory.heap.size=" + params.jbheap

        if params.jboffheap is not None:
            command = command + " jobmanager.memory.off-heap.size" + params.jboffheap

    if params.classentry is not None and params.jar is not None:
        command = command + " -c " + params.classentry + " " + params.jarpath + params.jar
    else:
        return reponse(code=303, data={'detail': "类或包不存在"}, message="failed")

    try:
        os.system(command)
        print(command)
    except:
        return reponse(code=304, data={'detail': "执行失败", 'command': command}, message="failed")
    finally:
        return reponse(data={'detail': params.classentry + "启动成功", 'command': command})


@app.post('/flink/download')
async def download(params: Params):
    if params.dwonpath != None:
        hdfscheck = hdfsupload.hdfscheck(params.dwonpath)
        return reponse(data={'detail': "操作成功", '状态': hdfscheck})
    else:
        return reponse(code=305, data={'detail': "执行失败"}, message="failed")


if __name__ == "__main__":
    uvicorn.run(app='flinkcommitserver:app', host='0.0.0.0', port=4096, reload=True, debug=True)
