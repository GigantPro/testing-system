from datetime import time
from time import sleep
import pytest

from string import printable, ascii_letters
from random import choice, randint
from httpx import AsyncClient

email = ''.join(choice(ascii_letters) for _ in range(randint(10, 20))) + '@example.com'
password = ''.join(choice(printable) for _ in range(randint(10, 50)))


@pytest.mark.asyncio
async def test_registration():
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.post('/register', json={'email': email, 'password': password})
        assert response.status_code == 200
