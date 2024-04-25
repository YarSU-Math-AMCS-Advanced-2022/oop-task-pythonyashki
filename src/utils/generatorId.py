import uuid


class CreatorID:
    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())