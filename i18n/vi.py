# -*- coding: utf-8 -*-
"""越南文词典：键为界面中文原文，值为越南文译文（占位符名称须与原文一致）。"""

MESSAGES = {
    # ------------------------------------------------------------ 通用词
    "红方": "Đỏ",
    "黑方": "Đen",
    "红": "Đỏ",
    "黑": "Đen",
    "你": "Bạn",
    "引擎": "Engine",
    "我方": "bên ta",
    "对方": "đối thủ",
    "未知": "Không rõ",
    "开局": "Khai cuộc",
    "、": ", ",
    "；": "; ",
    "。": ".",
    "{title}：{reason}": "{title}: {reason}",

    # ------------------------------------------------------------ 棋子名称
    "帅": "Tướng",
    "将": "Tướng",
    "仕": "Sĩ",
    "士": "Sĩ",
    "相": "Tượng",
    "象": "Tượng",
    "马": "Mã",
    "车": "Xe",
    "炮": "Pháo",
    "兵": "Tốt",
    "卒": "Tốt",

    # ------------------------------------------------------------ 局面校验 / 对局结果
    "{who}{name}超过 {lim} 个（当前 {n} 个）": "{who}: {name} vượt quá {lim} quân (hiện có {n})",
    "{who}缺少将/帅": "{who} thiếu Tướng",
    "将帅照面（同一路无遮挡），不是合法局面":
        "Hai Tướng đối mặt (cùng cột, không có quân cản), thế cờ không hợp lệ",
    "红兵不可能在己方底线": "Tốt Đỏ không thể nằm ở hàng cuối của bên mình",
    "黑卒不可能在己方底线": "Tốt Đen không thể nằm ở hàng cuối của bên mình",
    "{who}将/帅不在九宫内": "Tướng {who} nằm ngoài cung",
    "{who}（非行棋方）正被将军，轮次疑似有误":
        "{who} (bên không đến lượt) đang bị chiếu, có thể đã chọn sai lượt đi",
    "黑方胜（红帅被吃）": "Đen thắng (Tướng Đỏ bị ăn)",
    "红方胜（黑将被吃）": "Đỏ thắng (Tướng Đen bị ăn)",
    "被将死": "bị chiếu bí",
    "被困毙": "hết nước đi",
    "{winner}胜（{loser}{reason}）": "{winner} thắng ({loser} {reason})",
    "缺少将/帅（疑似残缺帧）": "Thiếu Tướng (nghi khung hình bị khuyết)",
    "缺少红帅（疑似残缺帧）": "Thiếu Tướng Đỏ (nghi khung hình bị khuyết)",
    "缺少黑将（疑似残缺帧）": "Thiếu Tướng Đen (nghi khung hình bị khuyết)",
    "棋盘框长宽比异常（{ratio:.2f}）": "Tỷ lệ khung bàn cờ bất thường ({ratio:.2f})",

    # ------------------------------------------------------------ 将军 / 绝杀 / 禁着
    "将军": "Chiếu tướng!",
    "绝杀": "Chiếu bí!",
    "困毙": "Hết nước!",
    "红方被将军": "Đỏ bị chiếu tướng",
    "黑方被将军": "Đen bị chiếu tướng",
    "长将": "trường chiếu",
    "长捉": "trường bắt",
    "一将一捉": "một chiếu một bắt",

    # ------------------------------------------------------------ 开局
    "默认（引擎选最优）": "Mặc định (engine chọn nước tốt nhất)",
    "{name}（{tip}）": "{name} ({tip})",
    "中炮（当头炮）": "Pháo đầu (Trung pháo)",
    "过宫炮": "Quá cung pháo",
    "士角炮": "Sĩ giác pháo",
    "巡河炮": "Tuần hà pháo",
    "起马局": "Khởi mã cục",
    "飞相局": "Phi tượng cục",
    "仙人指路": "Tiên nhân chỉ lộ",
    "双铁滑车": "Song thiết hoạt xa",
    "御驾亲征": "Ngự giá thân chinh",

    # ------------------------------------------------------------ 棋盘
    "楚  河": "SỞ HÀ",
    "汉  界": "HÁN GIỚI",
    "非法着法": "Nước đi không hợp lệ",
    "工具": "Công cụ",
    "擦除": "Xóa",
    "移动": "Di chuyển",
    "点击棋子将其擦除（也可右键）": "Bấm vào quân để xóa (hoặc chuột phải)",
    "先点棋子，再点目标格移动": "Bấm vào quân, rồi bấm ô đích để di chuyển",

    # ------------------------------------------------------------ 引擎分析面板
    "引擎分析": "Phân tích của engine",
    "评估：等待分析…": "Đánh giá: đang chờ phân tích…",
    "评估：{lead}": "Đánh giá: {lead}",
    "当前轮到：—": "Đến lượt: —",
    "当前轮到：<b>{who}</b>走子": "Đến lượt: <b>{who}</b> đi",
    "深度 --   NPS --": "Độ sâu --   NPS --",
    "深度 {depth}/{seldepth}   NPS {knps}k   置换表 {hashfull:.0f}%":
        "Độ sâu {depth}/{seldepth}   NPS {knps}k   Hash {hashfull:.0f}%",
    "候选着法（MultiPV，按红方视角评估）:": "Nước đi ứng viên (MultiPV, đánh giá theo góc nhìn bên Đỏ):",
    "着法记录:": "Biên bản ván cờ:",
    "{who} {n} 步内取胜": "{who} thắng trong {n} nước",
    "双方均势": "Hai bên cân bằng",
    "{who}领先 {lead:.2f}": "{who} dẫn trước {lead:.2f}",
    "红方胜率 {red:.0f}%\u3000·\u3000黑方胜率 {black:.0f}%":
        "Tỷ lệ thắng: Đỏ {red:.0f}%  ·  Đen {black:.0f}%",
    "（未设定我方执子）": "(Chưa chọn bên của bạn)",
    "你执{side}": "Bạn cầm quân {side}",
    "你执{side}：{txt}": "Bạn cầm quân {side}: {txt}",
    "你即将取胜": "Bạn sắp thắng",
    "你即将被将死": "Bạn sắp bị chiếu bí",
    "局势均势": "Thế cờ cân bằng",
    "你领先 {lead:.2f}": "Bạn dẫn trước {lead:.2f}",
    "你落后 {lead:.2f}": "Bạn đang kém {lead:.2f}",

    # ------------------------------------------------------------ 主窗口
    "象棋接管助手": "Trợ lý tiếp quản cờ tướng",
    "象棋接管助手 · Pikafish": "Trợ lý tiếp quản cờ tướng · Pikafish",
    "导入截图 (Ctrl+V)": "Nhập ảnh chụp (Ctrl+V)",
    "手动摆局": "Xếp cờ thủ công",
    "新开局": "Ván mới",
    "悔棋": "Đi lại",
    "翻转视角": "Lật bàn cờ",
    "持续引擎分析": "Engine phân tích liên tục",
    "引擎设置...": "Cài đặt engine...",
    "🎯 一键接管对局（自动找窗口·自动识别·自动走子）":
        "🎯 Tiếp quản ván cờ một chạm (tự tìm cửa sổ · tự nhận diện · tự đi quân)",
    "⏹ 停止接管（再点一次）": "⏹ Dừng tiếp quản (bấm lần nữa)",
    "开局走法:": "Khai cuộc:",
    "接管期间：轮到我方时优先走该开局的着法，走完（或不可行）后\n"
    "恢复引擎选最优。执黑时自动镜像。每局重新应用，直至停止接管。":
        "Khi tiếp quản: đến lượt bên ta thì ưu tiên đi theo khai cuộc này; đi hết (hoặc không đi được) thì\n"
        "quay lại để engine chọn nước tốt nhất. Cầm quân Đen sẽ tự đối xứng. "
        "Áp dụng lại mỗi ván cho đến khi dừng tiếp quản.",
    "对局窗口同步（高级·手动选择窗口）": "Đồng bộ cửa sổ ván cờ (nâng cao · chọn cửa sổ thủ công)",
    "刷新": "Làm mới",
    "开始观察": "Bắt đầu theo dõi",
    "停止观察": "Dừng theo dõi",
    "重新同步": "Đồng bộ lại",
    "自动续局（一局结束后自动点叉→再来一局）":
        "Tự động chơi tiếp (hết ván tự đóng popup → chơi ván nữa)",
    "对局结束后自动关闭结算弹窗并点「再来一局」，识别新开局后\n"
    "按“你的棋子在下方”自动判定阵营：你执红则先走，你执黑则等对方。":
        "Hết ván sẽ tự đóng popup kết quả và bấm «Chơi ván nữa»; nhận diện được ván mới thì\n"
        "xác định phe theo quy ước “quân của bạn ở phía dưới”: cầm Đỏ thì đi trước, cầm Đen thì chờ đối thủ.",
    "自动代点（轮到我方时直接在对局窗口落子）":
        "Tự động đi thay (đến lượt bên ta thì đi quân thẳng trong cửa sổ ván cờ)",
    "需先开始观察。引擎算出着法后自动在对局窗口点击落子；"
    "落子是否成功以窗口画面回读为准，未确认会提醒。":
        "Cần bắt đầu theo dõi trước. Engine tính xong sẽ tự bấm đi quân trong cửa sổ ván cờ; "
        "nước đi có thành công hay không được xác nhận qua hình ảnh cửa sổ, chưa xác nhận sẽ có cảnh báo.",
    "未连接。先设置好局面，再选择对局窗口开始观察。":
        "Chưa kết nối. Hãy thiết lập thế cờ trước, rồi chọn cửa sổ ván cờ để bắt đầu theo dõi.",
    "人机对战": "Đấu với máy",
    "接管分析": "Tiếp quản và phân tích",
    "我方执:": "Bên ta cầm:",
    "开始对战": "Bắt đầu đấu",
    "结束对战": "Kết thúc đấu",
    "文件(&F)": "&Tệp",
    "导入截图...": "Nhập ảnh chụp...",
    "退出": "Thoát",
    "就绪。点击「导入截图」开始半途接管。": "Sẵn sàng. Bấm «Nhập ảnh chụp» để tiếp quản giữa ván.",

    # 引擎
    "未找到 Pikafish（可用纯分析模式）": "Không tìm thấy Pikafish (các chức năng khác vẫn dùng được)",
    "未找到引擎：请运行 tools/download_engine.py 下载 Pikafish。识别与记录功能不受影响。":
        "Không tìm thấy engine: hãy chạy tools/download_engine.py để tải Pikafish. "
        "Chức năng nhận diện và ghi nước không bị ảnh hưởng.",
    "引擎已启动: {name}": "Engine đã khởi động: {name}",
    "引擎启动失败: {e}": "Khởi động engine thất bại: {e}",
    "引擎未响应 uciok，可能不是 UCI 引擎": "Engine không phản hồi uciok, có thể không phải engine UCI",
    "引擎进程异常退出，正在重启...": "Tiến trình engine thoát bất thường, đang khởi động lại...",
    "未知（局面看似合法）": "Không rõ (thế cờ có vẻ hợp lệ)",
    "⚠ 引擎无法分析当前局面（{reason}）。请用「重新同步」或「手动摆局」修正局面。":
        "⚠ Engine không phân tích được thế cờ hiện tại ({reason}). "
        "Hãy dùng «Đồng bộ lại» hoặc «Xếp cờ thủ công» để sửa thế cờ.",

    # 着法提示
    "建议着法: {move}{extra} — 请在 JJ 象棋上照此走子":
        "Nước gợi ý: {move}{extra} — hãy đi theo nước này trên JJ",
    "建议着法: {move}（{score}）— 请在 JJ 象棋上照此走子":
        "Nước gợi ý: {move} ({score}) — hãy đi theo nước này trên JJ",
    "（{score}, 深度 {depth}）": " ({score}, độ sâu {depth})",
    "（{score}）": " ({score})",
    "引擎走了: {move}（{score}）": "Engine đã đi: {move} ({score})",
    "对方最佳预测: {move}（{score}）": "Dự đoán nước tốt nhất của đối thủ: {move} ({score})",
    "预计算命中 ✓ 立即出着": "Đoán trúng nước đối thủ ✓ ra nước ngay",
    "开局走法：{move}": "Nước khai cuộc: {move}",
    "⚠ 检测到{kind}，已更换着法避免判负 ✓": "⚠ Phát hiện {kind}, đã đổi nước đi để tránh bị xử thua ✓",
    "⚠ 检测到{kind}，已强制更换着法避免判负 ✓":
        "⚠ Phát hiện {kind}, đã buộc đổi nước đi để tránh bị xử thua ✓",
    "⚠ 已陷入{kind}且无脱出着法，请手动走子！":
        "⚠ Đã rơi vào {kind} và không còn nước thoát, hãy tự đi quân!",

    # 自动代点
    "自动代点：{move}（{score}）— 正在落子，等待画面确认…":
        "Tự động đi thay: {move} ({score}) — đang đi quân, chờ hình ảnh xác nhận…",
    "⚠ 代点失败：对局窗口不可用。": "⚠ Đi thay thất bại: cửa sổ ván cờ không khả dụng.",
    "⚠ 落子位置被其它窗口遮挡，已放弃本次落子。请把对局窗口移到无遮挡的位置后重试。":
        "⚠ Vị trí đi quân bị cửa sổ khác che, đã bỏ qua nước này. "
        "Hãy di chuyển cửa sổ ván cờ đến chỗ không bị che rồi thử lại.",
    "落子未确认，自动重试：{move}…": "Nước đi chưa được xác nhận, tự thử lại: {move}…",
    "⚠ 代点的着法（{move}）重试后仍未确认。可能被弹窗/网络卡住，请手动检查 JJ。":
        "⚠ Nước đi thay ({move}) đã thử lại nhưng vẫn chưa được xác nhận. "
        "Có thể bị popup/mạng chặn, hãy tự kiểm tra JJ.",

    # 自动续局 / 新对局
    "已点「再来一局」，等待新开局…": "Đã bấm «Chơi ván nữa», chờ ván mới…",
    "已按坐标点「再来一局」，等待新开局…": "Đã bấm «Chơi ván nữa» theo tọa độ, chờ ván mới…",
    "新对局 ✓ 我方执{side}，先走…": "Ván mới ✓ Bên ta cầm quân {side}, đi trước…",
    "新对局 ✓ 我方执{side}，等对方先走…": "Ván mới ✓ Bên ta cầm quân {side}, chờ đối thủ đi trước…",
    "对局结束，等待新开局（自动点「再来一局」）…": "Ván cờ kết thúc, chờ ván mới (tự bấm «Chơi ván nữa»)…",
    "检测到结算界面 ✓ 正在自动点「再来一局」开下一局…":
        "Phát hiện màn hình kết quả ✓ đang tự bấm «Chơi ván nữa» để sang ván mới…",

    # 人机对战 / 对局操作
    "引擎未启动，无法对战。": "Engine chưa khởi động, không thể đấu.",
    "当前局面不合法：{problem}。\n请用「手动摆局」改正后再开始对战。":
        "Thế cờ hiện tại không hợp lệ: {problem}.\nHãy dùng «Xếp cờ thủ công» để sửa rồi bắt đầu đấu.",
    "对战开始：你执{side}。请走子。": "Bắt đầu đấu: bạn cầm quân {side}. Mời bạn đi.",
    "对战开始：你执{side}。引擎先走...": "Bắt đầu đấu: bạn cầm quân {side}. Engine đi trước...",
    "对战已结束。": "Đã kết thúc đấu.",
    "局面不合法：{problem}。请用「手动摆局」或重新导入截图并校对。":
        "Thế cờ không hợp lệ: {problem}. Hãy dùng «Xếp cờ thủ công» hoặc nhập lại ảnh chụp và kiểm tra.",
    "对战中不能移动引擎的棋子": "Khi đang đấu không thể di chuyển quân của engine",
    "非法着法: {move}": "Nước đi không hợp lệ: {move}",
    "，吃{side}{piece}": ", ăn {piece} {side}",
    "{who}走了：{move}{capture}": "{who} đã đi: {move}{capture}",
    "{who}着法已记录：{move}{capture}": "Đã ghi nước đi của {who}: {move}{capture}",
    "对局结束: {result}": "Ván cờ kết thúc: {result}",
    "新开局（初始局面）。可通过「导入截图」设置任意局面。":
        "Ván mới (thế cờ ban đầu). Có thể dùng «Nhập ảnh chụp» để đặt thế cờ bất kỳ.",
    "已悔棋": "Đã đi lại một nước",
    "拖入的内容不是可识别的图片": "Nội dung kéo vào không phải ảnh nhận diện được",
    "局面已摆好：我方执{side}。可直接「开始对战」，或继续摆子后再开始。":
        "Đã xếp xong thế cờ: bên ta cầm quân {side}. "
        "Có thể bấm «Bắt đầu đấu» ngay, hoặc tiếp tục xếp rồi mới bắt đầu.",
    "已接管局面：我方执{side}。对方走子后请在棋盘上把对方棋子拖到目标位置。":
        "Đã tiếp quản thế cờ: bên ta cầm quân {side}. "
        "Sau khi đối thủ đi, hãy kéo quân của đối thủ đến ô đích trên bàn cờ.",

    # 一键接管
    "正在自动寻找含棋盘的窗口…": "Đang tự động tìm cửa sổ có bàn cờ…",
    "枚举窗口失败: {e}": "Liệt kê cửa sổ thất bại: {e}",
    "检测到 {n} 个窗口处于最小化（如 MuMu 模拟器），请先还原窗口再点「一键接管」。":
        "Phát hiện {n} cửa sổ đang bị thu nhỏ (ví dụ trình giả lập MuMu), "
        "hãy khôi phục cửa sổ trước rồi bấm «Tiếp quản một chạm».",
    "没有可探测的窗口。请先打开 MuMu 并进入对局。": "Không có cửa sổ nào để dò. Hãy mở MuMu và vào ván cờ trước.",
    "探测窗口 {i}/{n}：{title} …": "Đang dò cửa sổ {i}/{n}: {title} …",
    "跳过窗口“{title}”：{reason}": "Bỏ qua cửa sổ “{title}”: {reason}",
    "画面识别失败": "nhận diện hình ảnh thất bại",
    "未找到含棋盘的窗口（{reason}）。请确认棋盘完整可见、无弹窗遮挡后重试。":
        "Không tìm thấy cửa sổ có bàn cờ ({reason}). "
        "Hãy đảm bảo bàn cờ hiện đầy đủ, không bị popup che rồi thử lại.",
    "未找到含棋盘的窗口。请确认已进入 JJ 对局界面（不是大厅），窗口未最小化，再重试。":
        "Không tìm thấy cửa sổ có bàn cờ. Hãy chắc chắn đã vào màn hình ván cờ JJ "
        "(không phải sảnh), cửa sổ không bị thu nhỏ, rồi thử lại.",
    "已取消接管。": "Đã hủy tiếp quản.",
    "初始化抓屏失败: {e}": "Khởi tạo chụp màn hình thất bại: {e}",
    "接管成功 ✓ 已锁定 {side}（窗口「{title}」已置顶）。":
        "Tiếp quản thành công ✓ đã khóa bên {side} (cửa sổ «{title}» đã được ghim trên cùng). ",
    "现在就轮到你，软件开始走子…": "Đến lượt bạn, phần mềm bắt đầu đi quân…",
    "等待对手走子，走完自动接管节奏。": "Đang chờ đối thủ đi, sau đó sẽ tự động tiếp nhịp.",

    # 窗口同步
    "（已最小化）": " (đã thu nhỏ)",
    "没有可选窗口。请先打开 MuMu/JJ 窗口再点「刷新」。":
        "Không có cửa sổ nào để chọn. Hãy mở cửa sổ MuMu/JJ trước rồi bấm «Làm mới».",
    "观察中：等待画面稳定以建立基准…": "Đang theo dõi: chờ hình ảnh ổn định để lập mốc…",
    "已停止观察。": "Đã dừng theo dõi.",
    "对局窗口已最小化，暂停同步（恢复窗口后自动继续）":
        "Cửa sổ ván cờ đã bị thu nhỏ, tạm dừng đồng bộ (khôi phục cửa sổ sẽ tự tiếp tục)",
    "⚠ 对局窗口已关闭。请重新打开 MuMu 并点「一键接管」。":
        "⚠ Cửa sổ ván cờ đã đóng. Hãy mở lại MuMu rồi bấm «Tiếp quản một chạm».",
    "对局窗口最小化，已自动恢复 ✓": "Cửa sổ ván cờ bị thu nhỏ, đã tự khôi phục ✓",
    "⚠ 对局窗口已最小化，自动恢复失败，请手动还原。":
        "⚠ Cửa sổ ván cờ bị thu nhỏ, tự khôi phục thất bại, hãy khôi phục thủ công.",
    "识别不到棋盘已 {minutes:.1f} 分钟——正在持续重试；如画面正常可点「重新同步」，或重开 JJ 对局后重新接管。":
        "Đã {minutes:.1f} phút không nhận diện được bàn cờ — đang liên tục thử lại; "
        "nếu màn hình bình thường có thể bấm «Đồng bộ lại», hoặc mở lại ván JJ rồi tiếp quản lại.",
    "对局窗口句柄已变化，已自动重新锁定 ✓": "Cửa sổ ván cờ đã thay đổi, đã tự động khóa lại ✓",
    "同步出错（已继续）: {e}": "Lỗi đồng bộ (đã tiếp tục): {e}",
    "未识别到棋盘（可能有弹窗/未进对局）。棋盘出现后自动恢复。":
        "Không nhận diện được bàn cờ (có thể có popup/chưa vào ván). Sẽ tự tiếp tục khi bàn cờ xuất hiện.",
    "子数骤降": "số quân giảm đột ngột",
    "画面持续无法识别（{reason}）——已按棋盘不可用处理":
        "Hình ảnh liên tục không nhận diện được ({reason}) — đã coi như bàn cờ không dùng được",
    "同步中（{n} 子，皮肤模板修正 {fixed} 处）": "Đang đồng bộ ({n} quân, mẫu skin đã sửa {fixed} chỗ)",
    "同步中（{n} 子）": "Đang đồng bộ ({n} quân)",
    "已锁定对局基准 ✓ 请确认左侧棋盘与 JJ 一致；之后双方着法将自动同步。":
        "Đã khóa mốc ván cờ ✓ Hãy xác nhận bàn cờ bên trái khớp với JJ; "
        "sau đó nước đi của hai bên sẽ tự đồng bộ.",
    "同步中（画面与棋盘一致）": "Đang đồng bộ (hình ảnh khớp với bàn cờ)",
    "对方落子中（落点暂不合法，等待画面稳定）…":
        "Đối thủ đang đặt quân (vị trí tạm thời chưa hợp lệ, chờ hình ảnh ổn định)…",
    "对方思考中（棋子已抬起）——落子后自动继续…":
        "Đối thủ đang suy nghĩ (đã nhấc quân) — đặt quân xong sẽ tự tiếp tục…",
    "⚠ 对方长时间未落子，请人工确认对局状态": "⚠ Đối thủ lâu không đặt quân, hãy tự kiểm tra trạng thái ván cờ",
    "该格复核为识别漏检，已保持棋盘不变 ✓": "Ô này được kiểm tra lại là nhận diện sót, đã giữ nguyên bàn cờ ✓",
    "检测到走子进行中/单格异常，等待稳定…（也支持你直接在 JJ 里手动走子）":
        "Phát hiện đang đi quân/một ô bất thường, chờ ổn định… (bạn cũng có thể tự đi quân trên JJ)",
    "已自动同步着法：{move}": "Đã tự đồng bộ nước đi: {move}",
    "⚠ 画面方向变化（红上↔红下）。请重新同步或重新导入。":
        "⚠ Hướng bàn cờ trên màn hình đã đổi (Đỏ trên ↔ Đỏ dưới). Hãy đồng bộ lại hoặc nhập lại.",
    "检测到局面不同步，正在自动校准…": "Phát hiện thế cờ không đồng bộ, đang tự hiệu chỉnh…",
    "捕获画面不完整，等待下一帧自动校准…": "Hình chụp chưa đầy đủ, chờ khung hình tiếp theo để tự hiệu chỉnh…",
    "检测到本地与 JJ 局面不一致，已自动以 JJ 为准重新同步 ✓（如反复出现请检查识别模型/皮肤模板）":
        "Phát hiện thế cờ ở đây khác với JJ, đã tự đồng bộ lại theo JJ ✓ "
        "(nếu lặp lại nhiều lần, hãy kiểm tra mô hình nhận diện/mẫu skin)",
    "抓屏失败，无法重新同步。": "Chụp màn hình thất bại, không thể đồng bộ lại.",
    "当前画面未识别到棋盘，无法重新同步。": "Không nhận diện được bàn cờ trên màn hình hiện tại, không thể đồng bộ lại.",
    "已重建同步基准 ✓ 棋盘与窗口一致，继续自动同步。":
        "Đã lập lại mốc đồng bộ ✓ bàn cờ khớp với cửa sổ, tiếp tục tự đồng bộ.",
    "已重建同步基准。⚠ 注意：窗口局面与左侧棋盘不一致，请用「悔棋」/「手动摆局」或重新导入截图把棋盘对齐，否则同步的着法可能不合法。":
        "Đã lập lại mốc đồng bộ. ⚠ Lưu ý: thế cờ trong cửa sổ khác với bàn cờ bên trái, "
        "hãy dùng «Đi lại»/«Xếp cờ thủ công» hoặc nhập lại ảnh chụp để căn chỉnh, "
        "nếu không các nước được đồng bộ có thể không hợp lệ.",

    # 设置
    "引擎设置": "Cài đặt engine",
    "界面语言": "Ngôn ngữ giao diện",
    "自动（优先中模型）": "Tự động (ưu tiên Mô hình vừa)",
    "中模型": "Mô hình vừa",
    "小模型": "Mô hình nhỏ",
    "万能带旋转": "Đa năng (hỗ trợ xoay)",
    "分析模式：每步用时 > 0 时按固定时间思考，否则按下面的深度上限。\n"
    "对战模式：每步用时上限（深度仍封顶于「深度」值，时间先到即停）。\n"
    "两者都是「时间 + 深度」双限制，时间到即出招，不会降低棋力上限。\n"
    "线程/置换表修改后需重启软件生效。":
        "Chế độ phân tích: thời gian mỗi nước > 0 thì nghĩ theo thời gian cố định, "
        "ngược lại theo giới hạn độ sâu bên dưới.\n"
        "Chế độ đấu: giới hạn thời gian mỗi nước (độ sâu vẫn bị chặn bởi giá trị «Độ sâu», "
        "hết giờ là dừng).\n"
        "Cả hai đều giới hạn kép «thời gian + độ sâu»: hết giờ là ra nước, không làm giảm sức cờ tối đa.\n"
        "Đổi số luồng/bảng băm cần khởi động lại phần mềm.",
    "思考线程数": "Số luồng suy nghĩ",
    "置换表大小": "Kích thước bảng băm (Hash)",
    "候选着法数 MultiPV": "Số nước ứng viên MultiPV",
    "深度上限": "Giới hạn độ sâu",
    "分析模式每步用时": "Thời gian mỗi nước (phân tích)",
    "对战模式每步用时": "Thời gian mỗi nước (đấu)",
    "截图识别模型": "Mô hình nhận diện ảnh",
    "拟人化鼠标（按真人轨迹移动，含加速/微抖/悬停）":
        "Chuột giống người (di chuyển theo quỹ đạo thật, có tăng tốc/rung nhẹ/dừng lơ lửng)",
    "最小急动度（平滑，推荐）": "Độ giật tối thiểu (mượt, khuyên dùng)",
    "物理模拟 WindMouse（弧线更明显）": "Mô phỏng vật lý WindMouse (đường cong rõ hơn)",
    "极快（不模拟轨迹，直接两次点击）": "Cực nhanh (không mô phỏng quỹ đạo, bấm thẳng hai lần)",
    "快": "Nhanh",
    "中": "Vừa",
    "慢": "Chậm",
    "轨迹算法": "Thuật toán quỹ đạo",
    "操作速度": "Tốc độ thao tác",
    "音效（抬子/落子/吃子/将军/绝杀锣声）":
        "Âm thanh (nhấc quân/đặt quân/ăn quân/chiếu tướng/tiếng chiêng chiếu bí)",
    "绝杀/困毙时语音播报": "Đọc giọng nói khi chiếu bí/hết nước",
    "识别模型：中模型精度最好（推荐，默认），小模型更快但实测精度略低，万能带旋转适合有旋转/透视的棋盘截图。":
        "Mô hình nhận diện: Mô hình vừa chính xác nhất (khuyên dùng, mặc định), "
        "Mô hình nhỏ nhanh hơn nhưng thực tế kém chính xác hơn một chút, "
        "Đa năng (hỗ trợ xoay) phù hợp với ảnh bàn cờ bị xoay/nghiêng.",
    "设置已保存（界面语言重启软件后生效）":
        "Đã lưu cài đặt (ngôn ngữ giao diện có hiệu lực sau khi khởi động lại phần mềm)",
    "设置已保存（线程/置换表重启后生效）":
        "Đã lưu cài đặt (số luồng/bảng băm có hiệu lực sau khi khởi động lại)",

    # ------------------------------------------------------------ 手动摆局
    "点选下方棋子 → 点击棋盘落子；右键擦除。支持「移动」工具拖动已有棋子。":
        "Chọn quân bên dưới → bấm lên bàn cờ để đặt; chuột phải để xóa. "
        "Dùng công cụ «Di chuyển» để dời quân có sẵn.",
    "设为开局": "Đặt thế khai cuộc",
    "清空": "Xóa hết",
    "翻转显示": "Lật hiển thị",
    "我方执子:": "Bên ta cầm quân:",
    "当前轮到:": "Đến lượt:",
    "红方 {n_red} 子，黑方 {n_black} 子（标准开局各 16 子）":
        "Đỏ {n_red} quân, Đen {n_black} quân (khai cuộc chuẩn mỗi bên 16 quân)",
    "⚠ 棋盘为空，请先摆放棋子": "⚠ Bàn cờ trống, hãy đặt quân trước",
    "⚠ 局面不合法：{problem}（请检查摆放）": "⚠ Thế cờ không hợp lệ: {problem} (hãy kiểm tra cách xếp)",

    # ------------------------------------------------------------ 一键接管对话框
    "一键接管 · 确认": "Tiếp quản một chạm · Xác nhận",
    "已找到对局窗口：「{title}」（识别 {n} 颗棋子）":
        "Đã tìm thấy cửa sổ ván cờ: «{title}» (nhận diện được {n} quân)",
    "检测到 红方在上方 —— 按惯例你的棋子在上半屏，推断你执{side}。":
        "Phát hiện Đỏ ở phía trên — theo quy ước quân của bạn ở nửa trên màn hình, "
        "suy ra bạn cầm quân {side}.",
    "检测到 红方在下方 —— 按惯例你的棋子在下半屏，推断你执{side}。":
        "Phát hiện Đỏ ở phía dưới — theo quy ước quân của bạn ở nửa dưới màn hình, "
        "suy ra bạn cầm quân {side}.",
    "我执（一般不用改，自动按 JJ 惯例推断）：":
        "Tôi cầm quân (thường không cần đổi, tự suy ra theo quy ước của JJ):",
    "自动推断：我执{side}": "Tự suy ra: tôi cầm quân {side}",
    "反过来：我执{side}（观战/代他人走时选这个）":
        "Ngược lại: tôi cầm quân {side} (chọn khi đang xem hoặc đi hộ người khác)",
    "现在轮到谁走：": "Bây giờ đến lượt ai:",
    "轮到我方（软件立即开始走子）": "Đến lượt bên ta (phần mềm bắt đầu đi ngay)",
    "轮到对方（等对手走完自动接上）": "Đến lượt đối thủ (chờ đối thủ đi xong rồi tự tiếp nhịp)",
    "开始接管": "Bắt đầu tiếp quản",
    "确认接管局面（一次性，约 10 秒）": "Xác nhận thế cờ tiếp quản (một lần, khoảng 10 giây)",
    "对照 JJ 真实局面：识别错的棋子——左边选棋子后点击棋盘修正（右键擦除）。全对就直接点 OK。":
        "Đối chiếu với thế cờ thật trên JJ: quân nào nhận diện sai — chọn quân trong bảng quân "
        "rồi bấm lên bàn cờ để sửa (chuột phải để xóa). Đúng hết thì bấm OK luôn.",
    "🔄 翻转棋盘（复刻盘与 JJ 上下相反时点这里，翻转后再逐格修正）":
        "🔄 Lật bàn cờ (bấm khi bàn cờ sao chép bị ngược trên/dưới so với JJ, lật xong rồi sửa từng ô)",
    "确认，开始下棋": "Xác nhận, bắt đầu chơi",

    # ------------------------------------------------------------ 导入截图
    "导入对局截图": "Nhập ảnh chụp ván cờ",
    "把截图拖到这里\n\n（也可以点下方「打开图片」或按 Ctrl+V 粘贴）":
        "Kéo ảnh chụp vào đây\n\n(hoặc bấm «Mở ảnh» bên dưới, hay nhấn Ctrl+V để dán)",
    "打开图片...": "Mở ảnh...",
    "粘贴截图 (Ctrl+V)": "Dán ảnh chụp (Ctrl+V)",
    "自动识别棋盘": "Tự nhận diện bàn cờ",
    "手动校准四角": "Hiệu chỉnh 4 góc thủ công",
    "重新识别棋子": "Nhận diện lại quân cờ",
    "步骤：载入截图 → 定位棋盘 → 校对识别结果 → 确认":
        "Các bước: tải ảnh chụp → định vị bàn cờ → kiểm tra kết quả nhận diện → xác nhận",
    "复刻棋盘（识别结果；用下方调色板点选棋子后点击棋盘修正）:":
        "Bàn cờ sao chép (kết quả nhận diện; chọn quân trong bảng quân bên dưới rồi bấm lên bàn cờ để sửa):",
    "清空棋盘": "Xóa bàn cờ",
    "截图红方在上（执黑时勾选，棋盘会随之翻转）": "Ảnh chụp có Đỏ ở trên (tích khi cầm quân Đen, bàn cờ sẽ lật theo)",
    "选择对局截图": "Chọn ảnh chụp ván cờ",
    "图片 (*.png *.jpg *.jpeg *.bmp *.webp);;所有文件 (*)":
        "Ảnh (*.png *.jpg *.jpeg *.bmp *.webp);;Tất cả tệp (*)",
    "导入": "Nhập ảnh",
    "无法读取该图片": "Không đọc được ảnh này",
    "剪贴板中没有可用的图片。\n可以用截图工具截图后按 Ctrl+V，或直接把图片文件拖进本窗口。":
        "Bộ nhớ tạm không có ảnh dùng được.\n"
        "Có thể chụp màn hình bằng công cụ chụp rồi nhấn Ctrl+V, hoặc kéo thả tệp ảnh vào cửa sổ này.",
    "松开鼠标即可导入该截图": "Thả chuột để nhập ảnh chụp này",
    "拖入的内容不是可识别的图片，请拖入截图文件":
        "Nội dung kéo vào không phải ảnh nhận diện được, hãy kéo tệp ảnh chụp vào",
    "左上角交点": "giao điểm góc trên trái",
    "右上角交点": "giao điểm góc trên phải",
    "右下角交点": "giao điểm góc dưới phải",
    "左下角交点": "giao điểm góc dưới trái",
    "请依次点击棋盘 {corners}": "Hãy lần lượt bấm vào {corners} của bàn cờ",
    "请点击 {corner}": "Hãy bấm vào {corner}",
    "手动校准完成，已识别棋子。请校对后确认。":
        "Đã hiệu chỉnh thủ công xong và nhận diện quân. Hãy kiểm tra rồi xác nhận.",
    "⚠ {error}\n可点「手动校准四角」重试，或直接在右侧调色板手动摆放。":
        "⚠ {error}\nCó thể bấm «Hiệu chỉnh 4 góc thủ công» để thử lại, hoặc tự xếp quân bằng bảng quân bên phải.",
    "⚠ 未识别出任何棋子。请直接用下方调色板手动摆放（或点「设为开局」后微调）。":
        "⚠ Không nhận diện được quân nào. Hãy tự xếp quân bằng bảng quân bên dưới "
        "(hoặc bấm «Đặt thế khai cuộc» rồi chỉnh lại).",
    "检测模型": "Mô hình phát hiện",
    "备用识别": "Nhận diện dự phòng",
    "备用识别（准确率较低）": "Nhận diện dự phòng (độ chính xác thấp hơn)",
    "⚠ {kind}只找到 {n} 个棋子，很可能不准。请对照左侧原图用调色板修正，或改用「手动摆局」。":
        "⚠ {kind} chỉ tìm thấy {n} quân, rất có thể không chính xác. "
        "Hãy đối chiếu với ảnh gốc bên trái và sửa bằng bảng quân, hoặc chuyển sang «Xếp cờ thủ công».",
    "{kind}识别出 {n} 个棋子": "{kind} nhận diện được {n} quân",
    "，{n} 格不确定": ", {n} ô không chắc chắn",
    "。请对照左侧原图核对，错处用调色板点选后点击棋盘修正。":
        ". Hãy đối chiếu với ảnh gốc bên trái, chỗ sai thì chọn quân trong bảng quân rồi bấm lên bàn cờ để sửa.",
    "皮肤模板已自动修正 {n} 处（棋盘上橙圈标注，请复核）":
        "Mẫu skin đã tự sửa {n} chỗ (khoanh tròn màu cam trên bàn cờ, hãy kiểm tra lại)",
    "皮肤模板已校准 {n} 类；点 OK 后会按本局继续更新模板":
        "Mẫu skin đã hiệu chỉnh {n} loại; bấm OK sẽ tiếp tục cập nhật mẫu theo ván này",
    "棋盘是空的，请先摆放棋子。": "Bàn cờ đang trống, hãy đặt quân trước.",
    "局面不合法：{problem}。\n请在右侧棋盘上用调色板修正（右键可快速擦除），再点 OK。":
        "Thế cờ không hợp lệ: {problem}.\n"
        "Hãy sửa trên bàn cờ bên phải bằng bảng quân (chuột phải để xóa nhanh), rồi bấm OK.",
    "✓ 已按本局更新皮肤模板（共 {n} 类），之后的识别会自动用它们校验。":
        "✓ Đã cập nhật mẫu skin theo ván này (tổng {n} loại), các lần nhận diện sau sẽ tự dùng để kiểm tra.",
    "（皮肤模板更新失败: {e}）": "(Cập nhật mẫu skin thất bại: {e})",

    # ------------------------------------------------------------ 截图识别
    "已按棋盘区域裁剪后识别": "Đã cắt theo vùng bàn cờ rồi nhận diện",
    "未找到检测模型（models/*.onnx），已改用备用识别，准确率较低。":
        "Không tìm thấy mô hình phát hiện (models/*.onnx), đã chuyển sang nhận diện dự phòng, "
        "độ chính xác thấp hơn.",
    "未能定位棋盘": "Không định vị được bàn cờ",
    "未在截图中定位到棋盘": "Không tìm thấy bàn cờ trong ảnh chụp",
    "检测模型执行失败: {e}": "Chạy mô hình phát hiện thất bại: {e}",
    "未找到检测模型，且备用识别未能定位棋盘。请运行 tools/download_models.py，或使用「手动摆局」":
        "Không tìm thấy mô hình phát hiện, và nhận diện dự phòng cũng không định vị được bàn cờ. "
        "Hãy chạy tools/download_models.py, hoặc dùng «Xếp cờ thủ công»",
    "检测模型对这张截图只找到 {n} 个棋子，已改用备用识别。建议核对，或使用「手动摆局」。":
        "Mô hình phát hiện chỉ tìm thấy {n} quân trong ảnh này, đã chuyển sang nhận diện dự phòng. "
        "Nên kiểm tra lại, hoặc dùng «Xếp cờ thủ công».",
    "皮肤模板修正了 {n} 处模型的判断，请重点复核": "Mẫu skin đã sửa {n} chỗ mô hình đoán sai, hãy kiểm tra kỹ",
    "有 {n} 处多个棋子落到同一格": "Có {n} chỗ nhiều quân rơi vào cùng một ô",
    "有 {n} 个棋子置信度偏低": "Có {n} quân có độ tin cậy thấp",

    # ------------------------------------------------------------ 程序入口
    "出错了": "Đã xảy ra lỗi",
    "发生未预期的错误，操作未完成：\n\n{error}\n\n详细信息已写入：\n{log}":
        "Đã xảy ra lỗi ngoài dự kiến, thao tác chưa hoàn tất:\n\n{error}\n\n"
        "Chi tiết đã được ghi vào:\n{log}",
}
