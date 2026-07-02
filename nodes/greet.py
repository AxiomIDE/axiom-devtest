from gen.messages_pb2 import GreetRequest, GreetReply
from gen.axiom_context import AxiomContext


def greet(ax: AxiomContext, input: GreetRequest) -> GreetReply:
    """Returns a friendly greeting for the given name, defaulting to "world"
    when no name is provided. A smoke-test node for the dev environment.
    """
    name = input.name.strip() or "world"
    ax.log.info("greeting", name=name)
    return GreetReply(message=f"Hello, {name}!")
