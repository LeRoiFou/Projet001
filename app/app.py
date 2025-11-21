from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory='app/templates')
app.mount(path='/static/', app=StaticFiles(directory='app/static'), name='static')

@app.get(
    path='/',
    summary='Default page',
    description="""
    Presentation page for the first project to be hosted in a cloud
    """,
)
def get_home(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request
        }
    )
    
@app.post(
    path='/',
    summary='First name information',
    description="""
    Name given by the user
    """,
)
async def post_home(request: Request):
    
    # Retrieve the value entered in the HTML file
    form = await request.form()
    
    # Convert the value retrieved into type dict to type str
    result = f"Bonjour {dict(form).get('first_name')} !"
    
    return templates.TemplateResponse(
        'index.html',
        {   
            'request': request,
            'result': result # value retrieved and returned to the HTML file
        }
    )

if __name__ == '__main__':
    uvicorn.run(app)
