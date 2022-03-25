from pydantic import BaseModel


# defines the POST request body template
class Request(BaseModel):
    key: str
    value: str

    def get_key_value(self):
        return self.key + ":" + self.value
