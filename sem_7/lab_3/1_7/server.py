import aiohttp
from aiohttp import web

async def echo_handler(request):
    data = await request.json()
    response_data = {"message": data["message"]}
    return web.json_response(response_data)

app = web.Application()
app.router.add_post('/echo', echo_handler)

web.run_app(app, host='localhost', port=8080)
