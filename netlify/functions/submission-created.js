/**
 * Send every new website request to Telegram the moment it arrives.
 *
 * Netlify calls this automatically whenever a form submission is stored; the
 * filename is the trigger, so it must stay `submission-created`. Both the
 * contact page and the lead card post to the `contact` form.
 *
 * Configured by environment variable (Netlify > Site configuration >
 * Environment variables), so it is safe to deploy before they exist:
 *   TELEGRAM_BOT_TOKEN   token of the LUMA SMART HOME bot (from @BotFather)
 *   TELEGRAM_CHAT_ID     the chat or group the bot posts into
 *
 * Nothing here may throw: the lead is already stored in Netlify Forms by the
 * time this runs, and a failed notification must never look like a lost lead.
 */

const esc = (s) =>
  String(s == null ? '' : s).replace(/[<>&]/g, (c) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]));

function telegramText(d) {
  const line = (label, value) => (value && String(value).trim() ? `\n<b>${label}:</b> ${esc(value)}` : '');
  const phone = String(d.phone || '').replace(/[^\d+]/g, '');
  const name = [d.first_name, d.last_name].filter(Boolean).join(' ');
  const fromCard = String(d.source_page || '').startsWith('lead card');
  const where = [d.address, d.city, d.zip].filter(Boolean).join(', ');
  return (
    (fromCard ? '🏠 <b>New walk-through request</b>' : '🏠 <b>New request from lumasmarthome.com</b>') +
    line('Name', name) +
    line('Phone', d.phone) +
    line('Email', d.email) +
    line('Where', where) +
    line('Type', d.inquiry) +
    line('Systems', d.systems) +
    line('Message', d.message) +
    line('Best way to reach', d.preferred_contact) +
    line('Found us', d.heard_from) +
    line('Page', d.source_page) +
    (phone ? `\n\n<a href="tel:${phone}">Call back</a>` : '')
  );
}

async function toTelegram(d) {
  const token = process.env.TELEGRAM_BOT_TOKEN;
  const chat = process.env.TELEGRAM_CHAT_ID;
  if (!token || !chat) return 'telegram: not configured';
  const res = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: chat, text: telegramText(d), parse_mode: 'HTML', disable_web_page_preview: true }),
  });
  return `telegram: ${res.status}`;
}

exports.handler = async (event) => {
  let d = {};
  try {
    const body = JSON.parse(event.body || '{}');
    d = (body.payload && body.payload.data) || {};
  } catch (e) {
    console.log('submission-created: unreadable payload');
    return { statusCode: 200, body: 'ok' };
  }
  if (d['bot-field']) return { statusCode: 200, body: 'ok' };
  try {
    console.log(await toTelegram(d));
  } catch (e) {
    console.log('telegram failed:', e && e.message);
  }
  return { statusCode: 200, body: 'ok' };
};

exports.telegramText = telegramText;
