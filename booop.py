from manim import *

class BooOp(Scene):
    def construct(self):

        p = Text("p")

        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10).move_to(4 * LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(2.5 * LEFT)
        t1 = Text("Boolean Operators", color = PINK, font_size = 38)
        
        self.play(Write(t1))
        self.wait(1)
        
        self.play(t1.animate.next_to(ellipse1, 2 * UP))
        A = Text("A", color = BLUE, font_size = 30)
        B = Text("B", color = RED, font_size = 30)
        A.next_to(ellipse1, LEFT).shift(DOWN)
        B.next_to(ellipse2, RIGHT).shift(DOWN)
        ells = VGroup(ellipse1, ellipse2, A, B)
 
        self.wait(1)

        t2 = Text("Take A and B to be sets.", color = PINK, font_size = 30)
        t2.shift(2 * RIGHT)

        self.play(Write(t2))
        self.wait(0.5)
        self.play(FadeOut(t2))
 
        self.wait(1)

        self.play(Write(ells))

        eq = MathTex(r"A \cap B", font_size = 28)
        eq1 = MathTex(r"A \cup B", font_size = 28)
        eq2 = MathTex(r" (A \cup B) - (A \cap B) ", font_size = 28)
        eq3 = MathTex(r"A - B", font_size = 28)

        self.wait(1)

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        eq.next_to(i, LEFT)
        self.play(FadeIn(intersection_text, eq))
        int = VGroup(intersection_text, eq, i)

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        eq1.next_to(u, LEFT)
        self.play(FadeIn(union_text, eq1))
        uni = VGroup(u, union_text, eq1)

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        eq2.next_to(e, LEFT)
        self.play(FadeIn(exclusion_text, eq2))
        excl = VGroup(exclusion_text, e, eq2)

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(eq1, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        eq3.next_to(d, LEFT)
        self.play(FadeIn(difference_text, eq3))

        self.play(FadeOut(ells))

        diff = VGroup(d, eq3, difference_text)
        self.play(diff.animate.shift(6 * LEFT, UP))

        e0 = Text("The difference of sets A and B is the set of", font_size = 21) 
        e00 = Text("all elements x such that x is in A and x is not in B.", font_size = 21)
        e0.next_to(d, DOWN)
        e00.next_to(e0, DOWN)
        e01 = Text("Mathematiclly we write:", font_size = 21)
        e02 = MathTex(r"A - B = \{x | x \in A \land x \notin B \}", font_size = 27)
        e01.next_to(e00, DOWN)
        e02.next_to(e01, DOWN)
        e0s = VGroup(e0, e00, e01, e02, diff)
        
        self.play(Write(e0))
        self.play(Write(e00))
        self.play(Write(e01))
        self.play(Write(e02))

        self.wait(2)
        self.play(FadeOut(e0s))
        self.wait(1)

        self.play(int.animate.move_to(diff))
        e2 = Text("The intersection of sets A and B is the set of", font_size = 21)
        e20 = Text("all elements x such that x is in A and x is in B.", font_size = 21)
        e21 = Text("Mathematically we write:", font_size = 21)
        e22 = MathTex(r"A \cap B = \{ x | x \in A \land x\in B \}", font_size = 27)
        e2.next_to(i, DOWN)
        e20.next_to(e2, DOWN)
        e21.next_to(e20, DOWN)
        e22.next_to(e21, DOWN)
        e2s = VGroup(int, e2, e20, e21, e22)

        self.play(Write(e2))
        self.play(Write(e20))
        self.play(Write(e21))
        self.play(Write(e22))

        self.wait(2)
        self.play(FadeOut(e2s))
        self.wait(1)

        self.play(uni.animate.move_to(diff))
        e3 = Text("The union of sets A and B is the set of", font_size = 21)
        e30 = Text("all elements x such that x is in A or x is in B.", font_size = 21)
        e31 = Text("Mathematically we write:", font_size = 21)
        e32 = MathTex(r"A \cup B = \{ x | x \in A \lor x \in B \}", font_size = 27)
        e3.next_to(u, DOWN)
        e30.next_to(e3, DOWN)
        e31.next_to(e30, DOWN)
        e32.next_to(e31, DOWN)
        e3s = VGroup(uni, e3, e30, e31, e32)

        self.play(Write(e3))
        self.play(Write(e30))
        self.play(Write(e31))
        self.play(Write(e32))

        self.wait(2)
        self.play(FadeOut(e3s))
        self.wait(1)

        self.play(excl.animate.move_to(diff))

        e1 = Text("The exclusion of sets A and B is the set of", font_size = 21)
        e10 = Text("all elements x such that x is in A or B and x is not in A and B.", font_size = 21)
        e11 = Text("Mathematically we write:", font_size = 21)
        e12 = MathTex(r"(A \cup B) - (A \cap B) = \{ x | x\in A \cup B \land x\notin A \cap B\}", font_size = 27)
        e1.next_to(e, DOWN)
        e10.next_to(e1, DOWN)
        e11.next_to(e10, DOWN)
        e12.next_to(e11, DOWN)
        e1s = VGroup(excl, e1, e10, e11, e12)

        self.play(Write(e1))
        self.play(Write(e10))
        self.play(Write(e11))
        self.play(Write(e12))

        self.wait(2)
        self.play(FadeOut(e1s))
        self.wait(1)

        self.play(t1.animate.move_to(p))
        self.wait(1)
        self.play(FadeOut(t1))


