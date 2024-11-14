from repositories.user_repository import user_repository
from services.user_service import user_service

result = user_service.validate("asd", "asdasdasd11", "asdasdasd1")
print(result)