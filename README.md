# Turtle Cleaning Services — quote request form

Live: https://cruedadiaz2-cpu.github.io/turtle-quote-calculator/
Link-in-bio page (for Instagram / Facebook): `/links/`

## How it works

The form runs entirely in the visitor's browser — there is no server and no
database. When someone finishes it, they send the summary themselves through one
of three routes, and it lands in `managturtlecs@gmail.com` or on WhatsApp:

- **Send by WhatsApp** → `wa.me` link to (908) 880-5716
- **Send by email** → the device's mail app (`mailto:`)
- **Open Gmail instead** → Gmail web compose, for devices with no mail app

Three routes because none of them works for everyone: `mailto:` needs a mail app
registered on the device, and Gmail web needs an active Google session. Each is
length-checked on its own, and **Copy details** is the fallback that always works.

No prices live in this page. Quotes are sent by reply — deliberately, so nothing
in the page source reveals the rate card.

## Editing it

Edit `src/page.html`, then:

    python src/build.py

That inlines the logos and writes `index.html`. Commit and push — GitHub Pages
redeploys in a couple of minutes.

Do **not** edit `index.html` directly; it is generated and your change would be
overwritten on the next build.

## Moving it to turtlecleaningusa.com

`index.html` is fully self-contained (logos included as data URIs), so it can be
uploaded on its own to any host. For a subdomain on GitHub Pages instead, add a
CNAME record pointing `cotiza` → `cruedadiaz2-cpu.github.io` at the DNS provider
(Hostinger), then set the custom domain in the repo's Pages settings — in that
order, or the live site goes down while DNS catches up.
