import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ── Korean font setup ──
from matplotlib import font_manager as fm
font_path = r'C:\Windows\Fonts\malgun.ttf'
font_bold_path = r'C:\Windows\Fonts\malgunbd.ttf'
fp = fm.FontProperties(fname=font_path)
fp_bold = fm.FontProperties(fname=font_bold_path)
plt.rcParams['font.family'] = fp.get_name()
plt.rcParams['axes.unicode_minus'] = False

# ── Figure setup ──
fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

# ── Background gradient ──
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack([gradient] * 256)
ax.imshow(gradient, extent=[0, 16, 0, 9], aspect='auto',
          cmap=matplotlib.colors.LinearSegmentedColormap.from_list('bg', ['#0f0c29', '#302b63', '#24243e']),
          zorder=0)

# ── Helper: draw a rounded box with glow ──
def draw_box(ax, x, y, w, h, color, label, sublabel=None, icon=None, fontsize=11):
    # Glow effect
    for i in range(3, 0, -1):
        glow = FancyBboxPatch((x - i*0.02, y - i*0.02), w + i*0.04, h + i*0.04,
                               boxstyle="round,pad=0.15", linewidth=0,
                               facecolor=color, alpha=0.08 * i, zorder=1)
        ax.add_patch(glow)
    # Main box
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                          linewidth=1.5, edgecolor=color, facecolor=color + '22',
                          zorder=2)
    ax.add_patch(box)
    # Icon
    if icon:
        ax.text(x + w/2, y + h*0.65, icon, fontsize=fontsize + 8,
                ha='center', va='center', color='white', zorder=3)
        ax.text(x + w/2, y + h*0.28, label, fontsize=fontsize,
                ha='center', va='center', color='white',
                fontproperties=fp_bold, zorder=3)
    else:
        ax.text(x + w/2, y + h*0.55, label, fontsize=fontsize,
                ha='center', va='center', color='white',
                fontproperties=fp_bold, zorder=3)
    if sublabel:
        ax.text(x + w/2, y + h*0.15, sublabel, fontsize=fontsize - 3,
                ha='center', va='center', color='#aaaacc',
                fontproperties=fp, zorder=3)

# ── Helper: draw arrow ──
def draw_arrow(ax, x1, y1, x2, y2, color='#6c63ff', style='->', bidir=False):
    if bidir:
        style = '<->'
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                             arrowstyle=style, color=color,
                             linewidth=2, mutation_scale=15,
                             connectionstyle="arc3,rad=0.0",
                             alpha=0.7, zorder=1)
    ax.add_patch(arrow)

# ══════════════════════════════════════
# Title
# ══════════════════════════════════════
ax.text(8, 8.35, '에이전트 오케스트레이션', fontsize=28,
        ha='center', va='center', color='white', fontproperties=fp_bold, zorder=5)
ax.text(8, 7.85, 'Agent Orchestration', fontsize=14,
        ha='center', va='center', color='#8888bb', fontproperties=fp, zorder=5)

# Decorative line under title
ax.plot([3, 13], [7.55, 7.55], color='#6c63ff', linewidth=2, alpha=0.5, zorder=5)

# ══════════════════════════════════════
# User (top)
# ══════════════════════════════════════
draw_box(ax, 6.5, 6.6, 3, 0.8, '#4fc3f7', '사용자 (User)', icon=None, fontsize=13)

# Arrow: User -> Orchestrator
draw_arrow(ax, 8, 6.6, 8, 5.95, color='#4fc3f7', bidir=True)

# ══════════════════════════════════════
# Orchestrator (center)
# ══════════════════════════════════════
orch_x, orch_y, orch_w, orch_h = 5.5, 4.6, 5, 1.3
# Special glow for orchestrator
for i in range(5, 0, -1):
    glow = FancyBboxPatch((orch_x - i*0.03, orch_y - i*0.03),
                           orch_w + i*0.06, orch_h + i*0.06,
                           boxstyle="round,pad=0.2", linewidth=0,
                           facecolor='#6c63ff', alpha=0.05 * i, zorder=1)
    ax.add_patch(glow)
box = FancyBboxPatch((orch_x, orch_y), orch_w, orch_h,
                      boxstyle="round,pad=0.2", linewidth=2.5,
                      edgecolor='#6c63ff', facecolor='#6c63ff22', zorder=2)
ax.add_patch(box)
ax.text(8, 5.55, '오케스트레이터', fontsize=18,
        ha='center', va='center', color='white', fontproperties=fp_bold, zorder=3)
ax.text(8, 5.1, 'Orchestrator  |  작업 분배 / 결과 통합 / 상태 관리',
        fontsize=9, ha='center', va='center', color='#bbbbdd', fontproperties=fp, zorder=3)
ax.text(8, 4.8, '(LLM 기반 의사결정 엔진)', fontsize=8.5,
        ha='center', va='center', color='#9999bb', fontproperties=fp, zorder=3)

# ══════════════════════════════════════
# Agents (bottom row)
# ══════════════════════════════════════
agents = [
    {'x': 0.5,  'label': '검색 에이전트',    'sub': 'Search Agent',     'color': '#ff7043', 'icon': None},
    {'x': 3.5,  'label': '코딩 에이전트',    'sub': 'Coding Agent',     'color': '#66bb6a', 'icon': None},
    {'x': 6.5,  'label': '분석 에이전트',    'sub': 'Analysis Agent',   'color': '#ffa726', 'icon': None},
    {'x': 9.5,  'label': '실행 에이전트',    'sub': 'Execution Agent',  'color': '#ab47bc', 'icon': None},
    {'x': 12.5, 'label': '메모리 에이전트',  'sub': 'Memory Agent',     'color': '#26c6da', 'icon': None},
]

agent_w, agent_h = 2.5, 1.3
agent_y = 1.8

for a in agents:
    draw_box(ax, a['x'], agent_y, agent_w, agent_h, a['color'],
             a['label'], sublabel=a['sub'], fontsize=10)
    # Arrow from orchestrator to agent
    agent_cx = a['x'] + agent_w / 2
    draw_arrow(ax, agent_cx, 4.6, agent_cx, agent_y + agent_h,
               color=a['color'], bidir=True)

# ══════════════════════════════════════
# Tools row (bottom)
# ══════════════════════════════════════
tools = ['Web / API', 'IDE / CLI', 'DB / Files', 'Shell / OS', 'Vector DB']
tool_y = 0.5
for i, (a, t) in enumerate(zip(agents, tools)):
    tx = a['x'] + agent_w / 2
    ax.text(tx, tool_y + 0.3, t, fontsize=8, ha='center', va='center',
            color='#888899', fontproperties=fp, zorder=3,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a2e', edgecolor='#444466', linewidth=0.8))
    draw_arrow(ax, tx, agent_y, tx, tool_y + 0.55, color='#555577')

# ══════════════════════════════════════
# Flow description (right side)
# ══════════════════════════════════════
desc_items = [
    ('1.', '사용자 요청 수신'),
    ('2.', '작업 분해 (Task Decomposition)'),
    ('3.', '적합한 에이전트에 위임'),
    ('4.', '병렬/순차 실행 관리'),
    ('5.', '결과 통합 및 응답'),
]

# No extra box — just subtle text at bottom-left is cleaner
# Actually let's skip this since the diagram is already self-explanatory

# ══════════════════════════════════════
# Save
# ══════════════════════════════════════
output_path = r'C:\Users\hwpar\OneDrive\퇴직준비세미나\Resources\agent_orchestration_slide.png'
plt.tight_layout(pad=0.5)
fig.savefig(output_path, dpi=150, bbox_inches='tight',
            facecolor='#0f0c29', edgecolor='none')
plt.close()
print('Saved: agent_orchestration_slide.png')
