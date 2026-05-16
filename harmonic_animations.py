"""
谐波科普动画 - 正弦波与谐波合成
使用ManimGL生成波形可视化动画
"""
from manimlib import *
import numpy as np

class SineWaveIntro(InteractiveScene):
    """第一章：认识正弦波 - 旋转矢量投射正弦波"""
    def construct(self):
        # 坐标系
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            width=12,
            height=5
        )
        axes.set_stroke_width(1)
        axes.set_color(GRAY)

        # 标签
        labels = VGroup(
            Tex("0", font_size=24),
            Tex("T/2", font_size=24),
            Tex("T", font_size=24),
            Tex("t", font_size=24),
        )
        labels[0].move_to(axes.c2p(0, -0.3))
        labels[1].move_to(axes.c2p(PI, -0.3))
        labels[2].move_to(axes.c2p(2*PI, -0.3))
        labels[3].move_to(axes.c2p(2*PI+0.3, -0.3))

        # 正弦波
        sine = FunctionGraph(
            lambda x: np.sin(x),
            x_range=[0, 2*PI],
            color=BLUE,
        )
        sine.set_stroke_width(3)

        # 标题
        title = Text("理想正弦波", font_size=36, color=BLUE)
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(0.5)
        self.play(ShowCreation(axes), Write(labels))
        self.wait(0.5)
        self.play(ShowCreation(sine), run_time=2)
        self.wait(1)

        # 标注关键参数
        peak_label = Text("峰值", font_size=24, color=YELLOW)
        peak_label.next_to(axes.c2p(PI/2, 1), UP)
        peak_dot = Dot(axes.c2p(PI/2, 1), color=YELLOW)

        period_arrow = Arrow(axes.c2p(0, -1.2), axes.c2p(2*PI, -1.2), color=GREEN)
        period_label = Text("周期 T = 0.02s", font_size=24, color=GREEN)
        period_label.next_to(period_arrow, DOWN)

        self.play(
            ShowCreation(peak_dot),
            Write(peak_label),
            run_time=1
        )
        self.wait(0.5)
        self.play(
            ShowCreation(period_arrow),
            Write(period_label),
            run_time=1
        )
        self.wait(2)


class FourierSynthesis(InteractiveScene):
    """第四章：谐波合成 - 逐步叠加展示"""
    def construct(self):
        title = Text("谐波合成：方波 = 基波 + 3次 + 5次 + 7次 + ...", font_size=30, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        # 坐标系
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.8, 1.8, 0.5],
            width=12,
            height=4
        )
        axes.set_stroke_width(1)
        axes.set_color(GRAY)
        axes.shift(DOWN)
        self.play(ShowCreation(axes))

        # 基波
        fundamental = FunctionGraph(
            lambda x: np.sin(x),
            x_range=[0, 2*PI],
            color=BLUE,
        )
        fundamental.set_stroke_width(3)

        fund_label = Text("基波 50Hz", font_size=24, color=BLUE)
        fund_label.to_corner(UR)

        self.play(ShowCreation(fundamental), Write(fund_label))
        self.wait(1)

        # 添加3次谐波
        harmonic3 = FunctionGraph(
            lambda x: np.sin(3*x) / 3,
            x_range=[0, 2*PI],
            color=RED,
        )
        harmonic3.set_stroke_width(2)

        sum13 = FunctionGraph(
            lambda x: np.sin(x) + np.sin(3*x)/3,
            x_range=[0, 2*PI],
            color=ORANGE,
        )
        sum13.set_stroke_width(3)

        h3_label = Text("+ 3次 150Hz", font_size=24, color=RED)
        h3_label.next_to(fund_label, DOWN, aligned_edge=LEFT)

        self.play(
            ShowCreation(harmonic3),
            Write(h3_label),
            run_time=1
        )
        self.wait(0.5)

        self.play(
            Transform(fundamental, sum13),
            FadeOut(harmonic3),
        )
        self.wait(1)

        # 添加5次谐波
        harmonic5 = FunctionGraph(
            lambda x: np.sin(5*x) / 5,
            x_range=[0, 2*PI],
            color=GREEN,
        )
        harmonic5.set_stroke_width(2)

        sum135 = FunctionGraph(
            lambda x: np.sin(x) + np.sin(3*x)/3 + np.sin(5*x)/5,
            x_range=[0, 2*PI],
            color=ORANGE,
        )
        sum135.set_stroke_width(3)

        h5_label = Text("+ 5次 250Hz", font_size=24, color=GREEN)
        h5_label.next_to(h3_label, DOWN, aligned_edge=LEFT)

        self.play(
            ShowCreation(harmonic5),
            Write(h5_label),
            run_time=1
        )
        self.wait(0.5)

        self.play(
            Transform(fundamental, sum135),
            FadeOut(harmonic5),
        )
        self.wait(1)

        # 添加7次谐波
        harmonic7 = FunctionGraph(
            lambda x: np.sin(7*x) / 7,
            x_range=[0, 2*PI],
            color=PURPLE,
        )
        harmonic7.set_stroke_width(2)

        sum1357 = FunctionGraph(
            lambda x: np.sin(x) + np.sin(3*x)/3 + np.sin(5*x)/5 + np.sin(7*x)/7,
            x_range=[0, 2*PI],
            color=ORANGE,
        )
        sum1357.set_stroke_width(3)

        h7_label = Text("+ 7次 350Hz", font_size=24, color=PURPLE)
        h7_label.next_to(h5_label, DOWN, aligned_edge=LEFT)

        self.play(
            ShowCreation(harmonic7),
            Write(h7_label),
            run_time=1
        )
        self.wait(0.5)

        self.play(
            Transform(fundamental, sum1357),
            FadeOut(harmonic7),
        )
        self.wait(1)

        # 最终接近方波
        result_label = Text("→ 越来越接近方波!", font_size=28, color=YELLOW)
        result_label.next_to(h7_label, DOWN, aligned_edge=LEFT)

        self.play(Write(result_label))
        self.wait(2)


class ThreePhaseRectifier(InteractiveScene):
    """第三章：三相整流器谐波产生"""
    def construct(self):
        title = Text("三相6脉波整流器 - 电流被'切'成方波", font_size=28, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        # 整流电路图示意（简化的）
        # 三相电压
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            width=12,
            height=3
        )
        axes.set_stroke_width(1)
        axes.set_color(GRAY)
        axes.shift(UP)

        # 三相电压
        colors = [BLUE, GREEN, RED]
        phases = [0, 2*PI/3, 4*PI/3]
        voltages = VGroup()
        for i, (phase, color) in enumerate(zip(phases, colors)):
            v = FunctionGraph(
                lambda x, p=phase: np.sin(x + p),
                x_range=[0, 2*PI],
                color=color,
            )
            v.set_stroke_width(2)
            voltages.add(v)

        self.play(ShowCreation(axes))
        self.play(*[ShowCreation(v) for v in voltages])
        self.wait(1)

        # 相电流（方波）
        current_axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            width=12,
            height=3
        )
        current_axes.set_stroke_width(1)
        current_axes.set_color(GRAY)
        current_axes.shift(2.5*DOWN)

        current_label = Text("A相电流波形（方波）", font_size=24, color=BLUE)
        current_label.next_to(current_axes, DOWN)

        # 近似方波（用傅里叶级数近似）
        def square_wave(x):
            s = 0
            for k in range(1, 20, 2):
                s += np.sin(k*x) / k
            return 1.2 * s / np.pi * 4

        current_wave = FunctionGraph(
            square_wave,
            x_range=[0, 2*PI],
            color=BLUE,
        )
        current_wave.set_stroke_width(3)

        self.play(
            ShowCreation(current_axes),
            Write(current_label)
        )
        self.wait(0.5)
        self.play(ShowCreation(current_wave), run_time=2)
        self.wait(1)

        # 频谱
        spectrum_label = Text("频谱：特征谐波 5次 7次 11次 13次...", font_size=24, color=YELLOW)
        spectrum_label.to_edge(DOWN)
        self.play(Write(spectrum_label))
        self.wait(2)


class TransformerSaturation(InteractiveScene):
    """第三章：变压器铁芯饱和谐波"""
    def construct(self):
        title = Text("变压器铁芯饱和 → 励磁电流尖顶波", font_size=28, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        # B-H 曲线
        bh_axes = Axes(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            width=5,
            height=5
        )
        bh_axes.set_stroke_width(1)
        bh_axes.set_color(GRAY)
        bh_axes.shift(3*LEFT + DOWN)

        bh_label = Text("B-H磁化曲线", font_size=20, color=WHITE)
        bh_label.next_to(bh_axes, UP)

        # B-H 曲线（sigmoid形状）
        bh_curve = FunctionGraph(
            lambda x: 1.5 * np.tanh(1.5*x),
            x_range=[-2, 2],
            color=ORANGE,
        )
        bh_curve.set_stroke_width(3)

        self.play(
            ShowCreation(bh_axes),
            Write(bh_label)
        )
        self.play(ShowCreation(bh_curve))
        self.wait(1)

        # 右侧 - 电流波形
        wave_axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-2, 2, 0.5],
            width=5,
            height=3
        )
        wave_axes.set_stroke_width(1)
        wave_axes.set_color(GRAY)
        wave_axes.shift(3*RIGHT + DOWN)

        wave_label = Text("励磁电流波形", font_size=20, color=WHITE)
        wave_label.next_to(wave_axes, UP)

        # 正常励磁电流（正弦）
        normal_current = FunctionGraph(
            lambda x: 0.5 * np.sin(x),
            x_range=[0, 2*PI],
            color=GREEN,
        )
        normal_current.set_stroke_width(2)

        self.play(
            ShowCreation(wave_axes),
            Write(wave_label)
        )
        self.play(ShowCreation(normal_current))
        self.wait(1)

        # 饱和后的尖顶波
        def peak_wave(x):
            s = np.sin(x)
            if s > 0.7:
                return 0.7 + 5*(s-0.7)**2
            elif s < -0.7:
                return -0.7 - 5*(abs(s)-0.7)**2
            return s

        saturation_current = FunctionGraph(
            peak_wave,
            x_range=[0, 2*PI],
            color=RED,
        )
        saturation_current.set_stroke_width(3)

        sat_label = Text("饱和后 → 尖顶波（3次谐波为主）", font_size=20, color=RED)
        sat_label.next_to(wave_axes, DOWN)

        self.play(
            Transform(normal_current, saturation_current),
            Write(sat_label),
            run_time=2
        )
        self.wait(2)
