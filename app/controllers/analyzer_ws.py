from fastapi import APIRouter, WebSocket
from stockfish import Stockfish

router = APIRouter(prefix="/ws", tags=["analysis"])

@router.websocket("/analysis")
async def websocket_analysis(websocket: WebSocket):
    await websocket.accept()


    stockfish = Stockfish("/usr/local/bin/stockfish/stockfish-ubuntu-x86-64-avx2")

    try:
        while True:
            data = await websocket.receive_json()

            fen = data.get("fen")

            if not fen:
                await websocket.send_json({"error": "FEN required"})
                continue

            if not stockfish.is_fen_valid(fen):
                await websocket.send_json({"error": "Invalid FEN"})
                continue

            stockfish.set_fen_position(fen)
            move = stockfish.get_best_move_time(1000)
            evaluation = stockfish.get_evaluation()

            await websocket.send_json({
                "move": move,
                "evaluation": evaluation,
            })

    except Exception:
        await websocket.close()
