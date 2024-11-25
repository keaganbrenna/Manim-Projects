from manim import *

class onefourtwo(Scene):
    def construct(self):
        
        text = MathTex(r"1 \times 142,857 = ", color = PINK)
        text1 = MathTex(r"2 \times 142,857 = ", color = PINK)
        text2 = MathTex(r"3 \times 142,857 = ", color = PINK)
        text3 = MathTex(r"4 \times 142,857 = ", color = PINK)
        text4 = MathTex(r"5 \times 142,857 = ", color = PINK)
        text5 = MathTex(r"6 \times 142,857 = ", color = PINK)

        texta = MathTex(r"142,857", color = PINK)
        text1a = MathTex(r"285,714", color = PINK)
        text2a = MathTex(r"428,571", color = PINK)
        text3a = MathTex(r"571,428", color = PINK)
        text4a = MathTex(r"714,285", color = PINK)
        text5a = MathTex(r"857,142", color = PINK)

        text.shift(UP * 2)
        text1.next_to(text, DOWN)
        text2.next_to(text1, DOWN)
        text3.next_to(text2, DOWN)
        text4.next_to(text3, DOWN)
        text5.next_to(text4, DOWN)

        texta.next_to(text, RIGHT)
        text1a.next_to(text1, RIGHT)
        text2a.next_to(text2, RIGHT)
        text3a.next_to(text3, RIGHT)
        text4a.next_to(text4, RIGHT)
        text5a.next_to(text5, RIGHT)

        a = VGroup(texta, text1a, text2a, text3a, text4a, text5a)
        
        self.play(Write(text), runtime = 1)
        self.play(Write(texta), runtime = 1)
        
        self.play(Write(text1), runtime = 1)
        self.play(Write(text1a), runtime = 1)
       
        self.play(Write(text2), runtime = 1)
        self.play(Write(text2a), runtime = 1)
        
        self.play(Write(text3), runtime = 1)
        self.play(Write(text3a), runtime = 1)
        
        self.play(Write(text4), runtime = 1)
        self.play(Write(text4a), runtime = 1)
        
        self.play(Write(text5), runtime = 1)
        self.play(Write(text5a), runtime = 1)
        self.wait(2)



        self.play(FadeOut(text, text1, text2, text3, text4, text5), a.animate.shift(LEFT * 7))

        text6 = Text("What do you notice about the numbers on the left?", color = PINK, font_size = 24)
        text6.shift(2 * RIGHT, UP)

        self.play(Write(text6))
        self.wait(3)

        text7 = Text("Multiplying by numbers up to 6 yield the same digits in the same order.", color = PINK, font_size = 24) 
        text8 = Text("Do any other numbers have this property?", color = PINK, font_size = 24)
        text7.next_to(text6, DOWN)
        text8.next_to(text7, DOWN)

        self.play(Write(text7))
        self.wait(3)
        self.play(Write(text8))
        self.wait(4)
        self.play(FadeOut(a), FadeOut(text6, text7, text8))
