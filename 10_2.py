from pydantic import BaseModel, HttpUrl, Field, root_validator
from requests import Session
from http import HTTPStatus


class _Body(BaseModel):
    markdown: str


class _Annotation(BaseModel):
    body: _Body


class _Context_for_display(BaseModel):
    before_html: str | None = Field(max_length=200)
    after_html: str | None = Field(max_length=200)


class _Referent(BaseModel):
    raw_annotatable_url: HttpUrl
    fragment: str
    context_for_display: _Context_for_display

    # @root_validator(values):
    #     if values[raw_annotatable_url] or

class _Web_page(BaseModel):
    canonical_url: HttpUrl | None
    og_url: HttpUrl | None
    title: str | None


class GeniusRequest(BaseModel):
    annotation: _Annotation
    referent: _Referent
    web_page: _Web_page


GeniusRequest(**{
  "annotation": {
    "body": {
      "markdown": "hello **world!**"
    }
  },
  "referent": {
    "raw_annotatable_url": "http://seejohncode.com/2014/01/27/vim-commands-piping/",
    "fragment": "execute commands",
    "context_for_display": {
      "before_html": "You may know that you can ",
      "after_html": " from inside of vim, with a vim command:"
    }
  },
  "web_page": {
    "canonical_url": None,
    "og_url": None,
    "title": "Secret of Mana"
  }
})


def get_response(data: GeniusRequest):
    with Session() as session:
        response = session.get(
            url='http://api.genius.com/web_pages/lookup?',
            params=data.dict()
        )
        if response == HTTPStatus.OK:
            return response.json()


data = GeniusRequest(markdown="hello **world!**",
                     raw_annotatable_url="http://seejohncode.com/2014/01/27/vim-commands-piping/",
                     fragment="execute commands", before_html="You may know that you can ",
                     after_html=" from inside of vim, with a vim command:",
                     title='Secret of Mana')
print(data)
print(get_response(data))

# 1. Как ввести сейчас аргументы в GeniusRequest, чтобы сработал get_response(data)?
# 2. В web_page один из ключей обязателен.
