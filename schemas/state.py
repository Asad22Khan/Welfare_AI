from typing import TypedDict, Optional


class ChatState(TypedDict):

    message: str

    user_role: Optional[str]

    intent: Optional[str]

    user_id: Optional[int]

    action_result: Optional[str]

    response: Optional[str]

    message: str

    intent: Optional[str]

    response: Optional[str]

    user_role: Optional[str]

    reference_id: Optional[str]