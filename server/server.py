from concurrent import futures
import grpc
import time
import chat_server_grpc_pb2_grpc
from chat_server_grpc_pb2_grpc import ChatServerServicer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    chat_server_grpc_pb2_grpc.add_ChatServerServicer_to_server(
        ChatServerServicer(),
        server)

    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()