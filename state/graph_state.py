from typing import TypedDict, Optional


class GraphState(TypedDict):

    user_id: Optional[str]
    message: str
    route: Optional[str]

    role: Optional[str]   # donor / donee / admin / surveyor

    response: Optional[str]

    metadata: Optional[dict]

    user_query: str
    name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    support_type: Optional[str]

    reference_id: Optional[str]
    response: Optional[str]