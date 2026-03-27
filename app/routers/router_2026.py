
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone
from pathlib import Path


template = Jinja2Templates(
    directory=str(Path(__file__).resolve(
    ).parent.parent / "templates" / "2026")
)


router = APIRouter(tags=["2026"])


today = datetime.now(timezone.utc)

year = today.year


def render_page(
    request: Request,
    name: str,
    active_page: str,
    page_css: str,
    page_title: str,
):
    return template.TemplateResponse(
        request=request,
        name=name,
        context={
            "year": year,
            "active_page": active_page,
            "page_css": page_css,
            "page_title": page_title,
        },
    )


@router.get("/")
def home(request: Request):
    return render_page(
        request=request,
        name="index.html",
        active_page="home",
        page_css="home.css",
        page_title="PyCon Togo 2026 — Home",
    )


@router.get("/speakers")
def speakers(request: Request):
    return render_page(
        request=request,
        name="2026_call_for_speakers_coming_soon.html",
        active_page="speakers",
        page_css="coming-soon.css",
        page_title="PyCon Togo 2026 — Call for Speakers (Opening Soon)",
    )


@router.get("/schedule")
def schedule(request: Request):
    return home(request)


@router.get("/venue")
def venue(request: Request):
    return home(request)


@router.get("/tickets")
def tickets(request: Request):
    return render_page(
        request=request,
        name="2026_tickets_coming_soon.html",
        active_page="tickets",
        page_css="coming-soon.css",
        page_title="PyCon Togo 2026 — Tickets (Opening Soon)",
    )


@router.get("/registration")
def registration(request: Request):
    return tickets(request)


@router.get("/contact")
def contact(request: Request):
    # TODO
    return render_page(
        request=request,
        name="2026_contact.html",
        active_page="contact",
        page_css="contact.css",
        page_title="PyCon Togo 2026 — Contact",
    )


@router.get("/about")
def about(request: Request):
    return render_page(
        request=request,
        name="2026_about.html",
        active_page="about",
        page_css="about.css",
        page_title="PyCon Togo 2026 — About",
    )


@router.get("/team")
def team(request: Request):
    return render_page(
        request=request,
        name="2026_teams.html",
        active_page="team",
        page_css="team.css",
        page_title="PyCon Togo 2026 — Team",
    )


@router.get("/teams")
def teams(request: Request):
    return team(request)


@router.get("/coc")
def coc(request: Request):
    return render_page(
        request=request,
        name="2026_coc.html",
        active_page="about",
        page_css="about.css",
        page_title="PyCon Togo 2026 — Code of Conduct",
    )


@router.get("/code-of-conduct")
def coc_slug(request: Request):
    return coc(request)


@router.get("/health_security")
def health_security(request: Request):
    return render_page(
        request=request,
        name="2026_health_security.html",
        active_page="about",
        page_css="about.css",
        page_title="PyCon Togo 2026 — Health & Safety Policy",
    )


@router.get("/health-safety")
def health_safety_slug(request: Request):
    return health_security(request)


@router.get("/sponsors")
def sponsors(request: Request):
    return render_page(
        request=request,
        name="2026_sponsors.html",
        active_page="sponsors",
        page_css="sponsors.css",
        page_title="PyCon Togo 2026 — Sponsors",
    )


@router.get("/cfp")
def cfp(request: Request):
    return speakers(request)


@router.get("/call-for-speakers")
def call_for_speakers(request: Request):
    return speakers(request)


@router.get("/volunteers")
def volunteers(request: Request):
    # TODO - create a volunteers page with a form to sign up as a volunteer
    pass


@router.get("/feedback")
def feedback(request: Request):
    # TODO - create a feedback page with a form to submit feedback
    pass


@router.get("/shop")
def shop(request: Request):
    # TODO - create a shop page with conference merchandise
    pass
