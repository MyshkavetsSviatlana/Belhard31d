from pydantic import BaseModel
from requests import Session
from http import HTTPStatus


def annotation(markdown):
    annotation = {"body": {"markdown": markdown}}
    return annotation


def referent(raw_annotatable_url, fragment, before_html, after_html):
    referent = {'raw_annotatable_url': raw_annotatable_url, 'fragment': fragment,
                'context_for_display': {'before_html': before_html, 'after_html': after_html}}
    return referent


def web_page(canonical_url, og_url, title):
    web_page = {"canonical_url": canonical_url, "og_url": og_url, "title": title}
    return web_page


class GeniusRequest(BaseModel):
    annotation: dict
    referent: dict
    web_page: dict


def get_response(data: GeniusRequest):
    with Session() as session:
        response = session.get(
            url='http://api.genius.com/web_pages/lookup?',
            params=data.dict()
        )
        if response == HTTPStatus.OK:
            return response.json()


data = GeniusRequest(annotation=annotation("hello **world!**"),
                     referent=referent("http://seejohncode.com/2014/01/27/vim-commands-piping/",
                                       "execute commands", "You may know that you can ",
                                       " from inside of vim, with a vim command:"),
                     web_page=web_page(None, None, 'Secret of Mana'))
print(data)
print(get_response(data))
