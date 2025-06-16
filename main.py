import random
import asyncio
from telegram import Bot
from datetime import datetime
import pytz

# 🔑 Configurações
TOKEN = '8046280889:AAF_fB24eoXB5QcteBwU8gGHrnC7kjk5ulA'
CHAT_ID = '-1002738022164'

# Definir o fuso horário de São Paulo
fuso_sp = pytz.timezone('America/Sao_Paulo')

bot = Bot(token=TOKEN)

# 🔗 Apenas criptoativos
pares = [
    "Bitcoin Cash", "Dogecoin", "Litecoin", "Pepe", "Shiba Inu", "Solana", "Toncoin", "Trump",
    "TRON", "Dogwifhat", "Bonk", "Ethereum", "Floki", "Bitcoin", "Ripple", "Binance Coin"
]

direcoes = ["↑ CALL - VAI SUBIR", "↓ PUT - VAI CAIR"]
expiracoes = ["M1", "M2", "M5", "M15"]

# 🎯 Relatório
wins = 0
losses = 0
total_operacoes = 0

async def enviar_sinal():
    global wins, losses, total_operacoes

    for i in range(5):  # Número de sinais na sessão
        par = random.choice(pares)
        direcao = random.choice(direcoes)
        expiracao = random.choice(expiracoes)
        hora_atual = datetime.now(fuso_sp).strftime('%H:%M')

        mensagem_entrada = (
            "🚨 *ENTRADA CRIPTO - GRATUITA* 🚨\n\n"
            f"🎯 *ATIVO:* {par} (OTC)\n"
            f"⏳ *TEMPO:* {expiracao}\n"
            f"📈 *DIREÇÃO:* {direcao}\n"
            f"⏰ *HORÁRIO:* {hora_atual}\n\n"
            "[👉 Opere agora](https://broker-qx.pro/sign-up/?lid=1372744)\n"
        )

        # Envia a mensagem e captura o ID
        msg = await bot.send_message(
            chat_id=CHAT_ID,
            text=mensagem_entrada,
            parse_mode="Markdown"
        )

        mensagem_id = msg.message_id

        # 🔗 Promoção do VIP a cada 2 sinais
        if i % 2 == 1:
            await bot.send_message(
    chat_id=CHAT_ID,
    text=(
        "💎 *ACESSO VIP LIBERADO!*\n\n"
        "🔥 Tenha acesso completo a todos os ativos: moedas, ações, índices e mais!\n"
        "🎯 Sinais com mais precisão, maior volume e acompanhamento em tempo real.\n\n"
        "✅ Resultados consistentes\n"
        "🚀 Suporte exclusivo\n"
        "🔐 Área de membros VIP\n\n"
        "👉 *Garanta sua vaga agora:* [SNIPER BINÁRIO VIP](https://sniperbinario.site/)"
    ),
    parse_mode="Markdown"
)


        await asyncio.sleep(900)  # Espera 15 min (simula operação)

        resultado = "WIN" if random.random() < 0.8 else "LOSS"

        if resultado == "WIN":
            wins += 1
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=open('./win.png', 'rb'),
                reply_to_message_id=mensagem_id
            )
        else:
            losses += 1
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=open('./loss.png', 'rb'),
                reply_to_message_id=mensagem_id
            )

        total_operacoes += 1
        await asyncio.sleep(30)

    taxa_acerto = (wins / total_operacoes) * 100 if total_operacoes > 0 else 0

    mensagem_relatorio = (
        "📊 *RELATÓRIO DA SESSÃO GRÁTIS*\n\n"
        f"✅ *WINS:* {wins}\n"
        f"❌ *LOSSES:* {losses}\n"
        f"🎯 *TAXA DE ACERTO:* {taxa_acerto:.2f}%\n"
        f"📈 *TOTAL DE OPERAÇÕES:* {total_operacoes}\n\n"
        "🚀 *Quer mais sinais? Confira o VIP!* 👉 [SNIPER BINÁRIO VIP](https://sniperbinario.site/)"
    )

    await bot.send_message(chat_id=CHAT_ID, text=mensagem_relatorio, parse_mode="Markdown")
    await asyncio.sleep(300)

    wins = 0
    losses = 0
    total_operacoes = 0

if __name__ == '__main__':
    asyncio.run(enviar_sinal())
