from manim import *
import numpy as np

class jaco(Scene):
    def construct(self):
        
        intro = Text("Let D be the region enclosed by the curve", color = PINK, font_size = 32)
        eq = MathTex(r"{{x}}^2 + {{y}}^2 = 1", color = PINK)
        intro.shift(2 * LEFT)
        eq.next_to(intro, RIGHT)
        fs = VGroup(intro, eq)

        self.play(Write(fs))
        self.wait(2)
        self.play(eq.animate.shift( 3 * UP), FadeOut(intro))

        self.wait(0.5)
        
        axes = Axes(
            x_range=[-2,2,1],
            y_range=[-2,2,1],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE},
            x_axis_config={
            "numbers_to_include": np.arange(-2, 2.01, 1),
            "numbers_with_elongated_ticks": np.arange(-2, 2.01, 1),
            },
            tips=False,
            y_axis_config={
            "numbers_to_include": np.arange(-2, 2.01, 1),
            "numbers_with_elongated_ticks": np.arange(-2, 2.01, 1),
            },
            )
        axes_labels = axes.get_axis_labels()
        plot = VGroup(axes, axes_labels)
        self.play(Write(plot), run_time=4, color = BLUE)
        
        curve_1 = axes.plot(lambda x: (1 - (x**2)) ** 0.5 , x_range=[-1, 1], color=PINK)
        curve_2 = axes.plot(lambda x: -(1 - (x**2)) ** 0.5 , x_range=[-1, 1], color=PINK)
        cs = VGroup(curve_1, curve_2)

        self.play(Write(cs))

        area = axes.get_area(curve_1, [-1, 1], bounded_graph=curve_2, color=PINK, opacity=0.5)

        self.play(FadeIn(area),run_time = 1)

        v = Arrow(start=0.5 * LEFT + 0.5 * UP, end= 2 * UP + 2 *LEFT, color=WHITE, buff = 2, tip_length=1/4)
        self.play(Write(v))

        ar = MathTex(r"Area", color = PINK)
        ar.shift(5/2 * UP, 5/2 * LEFT)
        self.play(Write(ar))
        self.play(ar.animate.shift(5/2*LEFT, 1/2 * UP), FadeOut(v))

        eqs = MathTex(r"=", color = PINK)
        eqs.next_to(ar, RIGHT)

        int = MathTex(r"\iint_D \ \,dy\, dx \\", color = PINK)
        int.next_to(eqs, RIGHT)

        self.play(Write(eqs))
        self.play(Write(int), run_time=1)

        set = VGroup(plot, cs, area)
        self.play(FadeOut(set))

        D = Text("Hold one variable constant (i.e. solve for x when y = 0)", color = PINK, font_size=34)
        self.play(Write(D))
        self.play(D.animate.shift(3/2 * UP))
        
        eq1 = MathTex(r"x^2 + 0 = 1", color = PINK, font_size = 34)
        self.play(Write(eq1))
        
        eq2 = MathTex(r"x = \pm 1", color = PINK, font_size = 34)
        eq2.align_to(eq)
        eq2.shift(DOWN)
        self.play(Write(eq2))

        self.play(eq2.animate.shift(5 * LEFT, UP), FadeOut(eq1, D))

        D1 = Text("Solve for y in terms of x", color = PINK, font_size = 34)
        self.play(Write(D1))
        self.play(D1.animate.shift(3/2 * UP))

        eq3 = MathTex(r"{{x^2 + y^2 = 1}}", color = PINK, font_size = 34)
        self.play(Write(eq3))

        eq4 = MathTex(r"{{y^2 = 1 - x^2}}", color = PINK, font_size = 34)
        eq4.align_to(eq3)
        eq4.shift(DOWN)
        self.play(Write(eq4))
        self.play(eq4.animate.shift(UP), FadeOut(eq3))

        eq5 = MathTex(r"{{y = \sqrt{1-x^2}}}", color = PINK, font_size = 34)
        eq5.align_to(eq4)
        eq5.shift(DOWN)
        self.play(Write(eq5))
        self.play(eq5.animate.shift(UP), FadeOut(eq4))

        eq6 = MathTex(r"y = \pm \sqrt{1 - x^2}", color = PINK, font_size = 34)
        eq6.align_to(eq5)
        eq6.shift(DOWN)
        self.play(Write(eq6))
        self.play(eq6.animate.shift(UP), FadeOut(eq5))
        self.play(eq6.animate.shift(5 * LEFT, DOWN), FadeOut(D1))

        eqg = VGroup(eq2, eq6)

        imp = MathTex(r"\implies", color = PINK, font_size = 34)
        imp.next_to(eqg, RIGHT)
        self.play(Write(imp))

        D2 = MathTex(r"D = \{ (x, y) | -1 \leq x \leq 1 , -\sqrt{1-x^2} \leq y \leq \sqrt{1-x^2} \}", color = PINK, font_size = 38)
        D2.next_to(imp, RIGHT)
        self.play(Write(D2))
        self.wait(3/2)

        self.play(D2.animate.shift(2 * UP, 2 * LEFT), FadeOut(imp, eqg))
        int1 = MathTex(r"\int_{-1}^{1} \int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} \,dy\, dx \\", color = PINK)

        eqs1 = MathTex(r"=", color = PINK)
        
        self.play(int.animate.shift(3 * DOWN), FadeOut(eqs, ar))
        eqs1.next_to(int, RIGHT)
        int1.next_to(eqs1, RIGHT)
        self.play(Write(eqs1))
        self.play(Write(int1))
        self.play(int1.animate.move_to(eq), FadeOut(int, D2, eqs1, eq))

        text = Text("This isn't very pretty", color = PINK, font_size = 32)
        text1 = Text("Let's change that", color = PINK, font_size = 32)
        self.play(Write(text))
        text1.align_to(text)
        text1.shift(DOWN)
        self.play(Write(text1))
        self.wait(1)
        self.play(FadeOut(text, text1))
        
        self.play(set.animate.shift(2 * LEFT), FadeIn(set))
        set1 = VGroup(set, int1) 
        self.play(set1.animate.shift(7/2 * LEFT))
        
        Tmap = MathTex(r"T", color = PINK)
        map = MathTex(r"\mapsto", color = PINK)

        map.align_to(set)
        map.next_to(set, 3/2 * RIGHT)
        Tmap.align_to(map)
        Tmap.next_to(map, UP)
        maps = VGroup(map, Tmap)
        self.play(Write(maps))

        pax = PolarPlane(
            azimuth_units="PI radians",
            azimuth_step = 12,
            azimuth_label_font_size=32,
            size=5,
            radius_max=2,
            radius_config={"font_size": 32},
        ).add_coordinates(r_values=None)
        pax.shift(4 * RIGHT) 
        self.play(Write(pax))

        xy = MathTex(r"F(x,y)", color = PINK)
        rt = MathTex(r"F(r,\theta)", color = PINK)
        self.play(maps.animate.shift(2 * LEFT), FadeOut(set), )
        xy.next_to(maps, LEFT)
        rt.next_to(maps, RIGHT)
        self.play(Write(xy), Write(rt))

        xyrt = VGroup(xy, rt)

        text2 = Text("T is a trasformation that maps coordinates (x, y)", color = PINK, font_size=24) 
        text3= Text("to a distance from the origin r at some angle theta ", color = PINK, font_size = 24)
        text2.align_to(maps)
        text2.next_to(maps, DOWN)
        text2.shift( LEFT, 1/4 * DOWN)
        text3.align_to(text2)
        text3.next_to(text2, DOWN)
        self.play(Write(text2), Write(text3))
        self.wait(3)
        self.play(FadeOut(text2, text3))

        self.play(int1.animate.shift(4*LEFT),xyrt.animate.shift(5/2 * UP, 3/2 * RIGHT),maps.animate.shift(5/2*UP, 3/2 * RIGHT) )

        p = np.array([0,0,0])
        p1 = np.array([1.25, 0, 0])
        p2 = np.array([1.25, 5/4 *(3**0.5), 0])

        conv = Polygon(p, p1, p2, color = PINK)
        conv.align_to(pax)
        conv.shift(4 * RIGHT)
        self.play(Write(conv), run_time=2)
        self.wait(1)
        
        self.play(conv.animate.shift(7 * LEFT, 3/2 * DOWN))
        self.play(ScaleInPlace(conv, 2))

        ir = MathTex(r"{{r}}", color = PINK)
        ir.align_to(conv)
        x = MathTex(r"{{x}}", color = PINK)
        x.align_to(conv)
        y = MathTex(r"{{y}}", color = PINK)
        y.align_to(conv)
        theta = MathTex(r"{{\theta}}", color = PINK)
        ir.shift(3 * LEFT, 1/2 * DOWN)
        x.shift(5/2 * LEFT, 3 * DOWN)
        y.shift(3/4 *LEFT, 1/2 * DOWN)
        theta.shift(11/4 * LEFT, 2 * DOWN)
        ir1 = MathTex(r"{{r}", color = PINK)
        ir1.move_to(ir)
        theta1 = MathTex(r"{{\theta}}", color = PINK)
        theta1.move_to(theta)
        tris = VGroup(ir, x, y, theta, ir1, theta1)
    
        line = Line(p, p1)
        line1 = Line(p, p2)
        lines = VGroup(line, line1)
        lines.shift(3.64 * LEFT, 2.585 * DOWN)
        
        angle = Angle(line, line1, radius = 0.75, color = PINK)
        self.play(Write(tris), Create(angle), run_time=1)
        
        self.wait(1)

        peq = MathTex(r"{{{x}} \over {{r}}}", r"=", r"cos(\theta)", color = PINK)
        peq1 = MathTex((r"{{{y}} \over  {{r}}}"), r"{{=}}", r"{{sin(\theta)}}", color = PINK)

        peq.shift(3 * LEFT,  UP)
        peq1.next_to(peq, DOWN)

        tar = MathTex(r"1", color = BLACK)
        tar1 = MathTex(r"1", color = BLACK)
        tar2 = MathTex(r"1", color = BLACK, font_size=1)
        tar3 = MathTex(r"1", color = BLACK, font_size=1)
        tar4 = MathTex(r"1", color = BLACK, font_size = 1)

        tar.shift(4 * LEFT, 2 * UP)
        tar1.shift(2 * LEFT, 2 * UP)
        tar2.shift(4 * LEFT)
        tar3.shift(2 * LEFT)
        tar4.shift(4 * LEFT, 1/2 * DOWN)
        
        tars = VGroup(tar, tar1, tar2, tar3, tar4)

        equations = VGroup(peq, peq1)

        feq = MathTex(r"{{x}}", r"=", r"{{r}}cos(\theta)" , color = PINK)
        feq1 = MathTex(r"{{y}}",r"=", r"{{r}}sin(\theta)", color = PINK)
        ref = MathTex(r"=", color = BLACK)

        feq.move_to(peq)
        feq1.move_to(peq1)
        ref.shift(3/2 * UP, 3 * LEFT)

        self.play(FadeOut(conv, angle))
        self.play(FadeIn(equations), TransformMatchingTex(x, tar),TransformMatchingTex(ir, peq), TransformMatchingTex(y, tar2),TransformMatchingTex(ir1, tar4) , TransformMatchingTex(theta, tar1), TransformMatchingTex(theta1, tar3), run_time=1)
        self.play(TransformMatchingTex(peq, feq), TransformMatchingTex(peq1, feq1), FadeOut(tars))
        self.play(feq.animate.next_to(ref, LEFT), feq1.animate.next_to(ref, RIGHT))

        drb = MathTex(r"{{x}}^2", r"+", r"{{y}}^2", r"=",r"1", color = PINK)

        drb.shift(3 * LEFT)
        self.play(Write(drb))

        trig1 = MathTex(r"rcos(\theta)", color = PINK, fill_opacity=0.5)
        trig2 = MathTex(r"rsin(\theta)", color = PINK, fill_opacity=0.5)
        trigs = VGroup(trig1, trig2).arrange_submobjects().shift(UP)

        drb1 = MathTex(r"({{rcos(\theta)}})^2", r"+", r"({{rsin(\theta)}})^2", r"=", r"1", color = PINK)
        drb0 = MathTex(r"({{r}}^2", r"{{cos(\theta)}}^2", r"+", r"{{r}}^2", r"{{sin(\theta)}}^2)", r"=", r"1", color = PINK)
        drb2 = MathTex(r"{{r}}^2", r"({{cos(\theta)^2", r"+", r"sin(\theta)^2)", r"=", r"1", color = PINK)
        
        drb1.shift(3 * LEFT)
        trigs.shift(3 * LEFT)
        drb2.shift(3 * LEFT)
        drb0.shift(3 * LEFT)
        drb3 = MathTex(r"{{r}}^2", r"({1})", r"=", r"1", color = PINK)
        drb3.shift(3 * LEFT)
        drb4 = MathTex(r"r", r"{{=}}", r"1", color = PINK)
        drb4.shift(4 * LEFT)

        self.play(TransformMatchingTex(Group(drb, trigs), drb1))
        self.wait(0.5)
        self.play(TransformMatchingTex(drb1, drb0))
        self.wait(0.5)
        self.play(TransformMatchingTex(drb0, drb2))
        self.wait(0.5)
        self.play(TransformMatchingTex(drb2, drb3))
        self.wait(0.5)
        self.play(TransformMatchingTex(drb3, drb4))

        note = Text("Notice that we keep r positive", color = PINK, font_size=34)
        note.shift(3 * LEFT, DOWN)

        self.play(Write(note))
        self.wait(0.5)
        self.play(FadeOut(note))

        circle = Circle(radius = 1.25, stroke_color = PINK, fill_color = PINK, fill_opacity = 0.75, stroke_width = 5)

        circle.align_to(pax)
        circle.shift(4 * RIGHT)
        self.play(DrawBorderThenFill(circle), run_time=3)

        thetarange = MathTex(r"0 \leq \theta \leq 2\pi", color = PINK)
        thetarange.next_to(drb4, 2 * RIGHT)
        thetarange.shift(1/2 * UP)

        self.play(Write(thetarange),drb4.animate.shift(1/2 * LEFT, 1/2 * UP))
        
        thetrs = VGroup(drb4, feq, feq1, thetarange)
        temp = VGroup(xy, rt, map, Tmap)
        
        self.play(FadeOut(int1),thetrs.animate.shift(3/2 * UP), temp.animate.shift(5/2 * LEFT, 3 * DOWN))

        dxdy = MathTex(r"dxdy", color = PINK)
        ques = MathTex(r"?", color = PINK)

        dxdy.move_to(xy)
        ques.move_to(rt)

        self.play(FadeOut(xy, rt), FadeIn(dxdy, ques))

        self.wait(1)

        self.play(FadeOut(dxdy, ques, map ,Tmap))

        diff = MathTex(r"\partial(x, y)", r"\over", r"\partial(r,\theta)", color = PINK)

        diff.shift(LEFT * 11/2)
        
        equal = MathTex(r"=", color = PINK)
        equal.next_to(diff, RIGHT)
        m = Matrix([[r"{{cos\theta}}", r"{{sin\theta}}"],[r"{{-rsin\theta}}", r"{{rcos\theta}}"]]).set_color(PINK)
        m.next_to(equal, 2 * RIGHT)
        
        self.play(Write(diff), Write(equal), Write(m))

        m1 = MathTex(r"{{(rcos(\theta)^2}}", r"+", r"{{rsin(\theta)^{2})}}", color = PINK)
        m1.move_to(m)

        self.play(TransformMatchingShapes(m,m1))
        self.wait(1)


        m3 = MathTex(r"{{r}}",r"{{(cos(\theta)^2}}", r"+", r"{{sin(\theta)^{2})}}", color = PINK)
        m3.shift(2 * DOWN, 2 * LEFT)
        
        self.play(TransformMatchingShapes(m1, m3))
        self.wait(1)
        
        m4 = MathTex(r"{{r}}{{(1)}}", color = PINK)
        m4.move_to(m3)

        self.play(TransformMatchingShapes(m3, m4))
        self.wait(1)

        m5 = MathTex(r"r", color = PINK)
        m5.move_to(m4)

        self.play(TransformMatchingTex(m4, m5))

        self.play(m5.animate.next_to(equal, RIGHT))
        
        self.wait(0.75)

        m6 = MathTex(r"{{rdrd\theta}}", color = PINK)
        m6.move_to(ques)

        self.play(FadeOut(diff, equal), m5.animate.move_to(ques), FadeIn(dxdy, Tmap, map), TransformMatchingShapes(m5, m6))
        
        self.wait(0.75)

        self.play(m6.animate.shift(UP, 2 * LEFT), FadeOut(map, Tmap, dxdy))

        fint = MathTex(r"\int_{0}^{2\pi} \int_{0}^{1} r\,dr\, d\theta \\", color = PINK)
        fint.shift(2 * LEFT, 1/2 * DOWN)
        self.wait(0.75)
        self.play(Write(fint))

        eva = MathTex(r"Evaluate", color = PINK)
        eva.shift(3/2 * LEFT)
        
        self.play(FadeOut(m6, thetarange, feq, feq1, drb4, pax, circle), Write(eva), fint.animate.next_to(eva, RIGHT))








        
        
        






