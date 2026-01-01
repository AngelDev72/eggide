from aiohttp import web

async def status(request):
    return web.json_response({
        "app": "EGGIDE",
        "status": "alive",
        "mode": "mobile-dev"
    })

app = web.Application()
app.router.add_get("/status", status)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8000)
