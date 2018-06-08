import grpc
import time

import chat_server_grpc_pb2_grpc
import chat_server_grpc_pb2


def generate_input_messages():
    """

    :return:
    """
    msgs = ["Helloworld", "BigBasket", "Now"]
    for msg in msgs:
        time.sleep(2)
        yield chat_server_grpc_pb2.Request(message=msg)


def run():
    """

    :return:
    """
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_server_grpc_pb2_grpc.ChatServerStub(channel)
    print("Chat server-----------")
    responses = stub.Communicate(generate_input_messages())
    print("responses: ")
    for response in responses:
        print(response.message)


if __name__ == '__main__':
    run()