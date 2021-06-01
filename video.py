class DarwinIntro(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        circle.set_fill(WHITE, opacity=1)
        circle.set_stroke(WHITE, width=4)
        d = Tex(r"D").get_grid(1, 1, height=3)
        self.play(ShowCreation(square), lag_ratio=0.01, run_time=3)
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.scale(2))
        self.wait()
        self.play(ReplacementTransform(circle, triangle))
        self.wait()
        self.play(triangle.animate.scale(1.5))
        self.wait()
        self.play(triangle.animate.rotate(PI / 1.5))
        self.play(ReplacementTransform(triangle, d))
        self.play(d.animate.shift(4*LEFT))
        self.wait()
        source = Text("arwin Tech", font_size=50, line_spacing=1).shift(DOWN+0.9*LEFT)
        target = Text("Learn.Bulid.Share", font_size=50, line_spacing=1).shift(DOWN+0.5*RIGHT)
        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()

class BinarySearchText(Scene): 
    def construct(self):
        text = Text("""
         def binary_search(arr, x):
             
                low = 0
                 
                high = len(arr) - 1

                mid = 0

                while low <= high:

                    mid = (high + low) // 2

                    if arr[mid] < x:

                        low = mid + 1

                    elif arr[mid] > x:

                        high = mid - 1

                    else:

                        return mid

                return -1
            """, font_size=30, line_spacing=0.5)
        self.play(Write(text, run_time=6))
        self.wait(5)
        self.play(FadeOut(text))

class BinarySearch(Scene):
    def construct(self):
        intro_words = Text("""
       Binary Search 
        """, gradient=(BLUE, BLUE_D)).scale(2)
        intro_words.to_edge(UP)
        self.play(Write(intro_words, run_time=6))
        self.play(FadeOut(intro_words))
        self.wait(2)
        unsorted = Text("[3, 9, 4, 7, 9, 1, 14, 11]", font_size=50, line_spacing=1)
        sorted_list = Text("[1, 3, 4, 7, 9, 11, 14]", font_size=50, line_spacing=1)
        number_to_find = Text("# we're looking for: 4")
        number_to_find.to_edge(UP)  
        list_two = Text("[1, 3, 4]")
        self.play(Write(unsorted, run_time=3))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(unsorted, sorted_list, **kw))
        self.wait()
        self.play(Write(number_to_find, run_time=2))
        self.wait(2)
        self.play(FadeOut(number_to_find))
        circ = Circle(radius=0.5).set_color(BLUE_D).shift(LEFT*0.3)
        midpoint = Text("Midpoint").shift(DOWN*3)
        arrow_1 = Arrow(start=DOWN, end=UP, color=GOLD).shift(DOWN*1.6+LEFT*0.3)
        self.play(DrawBorderThenFill(circ))
        self.play(DrawBorderThenFill(arrow_1))
        self.play(Write(midpoint, run_time=2))
        self.wait(2)
        self.play(FadeOut(arrow_1))
        self.play(FadeOut(midpoint))
        self.wait(3)
        self.play(FadeOut(circ))
        self.wait()
        line2 = Line(UP*1.5, DOWN*1.5).shift(LEFT*0.8)
        dline2 = DashedVMobject(line2).set_color(BLUE_D)
        self.play(ShowCreation(dline2))
        self.wait(2)
        rec = Rectangle(width=3.75).set_color(BLUE_D).shift(LEFT*2.75)
        self.play(FadeOut(dline2))
        self.play(DrawBorderThenFill(rec))
        self.wait(3)
        self.play(FadeOut(rec))
        self.play(TransformMatchingShapes(sorted_list, list_two, **kw))
        self.wait()
        circ2 = Circle(radius=0.5).set_color(BLUE_D)
        midpoint_2 = Text("Midpoint").shift(DOWN*3)
        arrow_2 = Arrow(start=DOWN, end=UP, color=BLUE_D).shift(DOWN*1.6)
        self.play(DrawBorderThenFill(circ2))
        self.play(DrawBorderThenFill(arrow_2))
        self.play(Write(midpoint_2, run_time=2))
        self.play(FadeOut(arrow_2))
        self.play(FadeOut(midpoint_2))
        self.wait()
        self.play(FadeOut(circ2))
        self.wait()
        line3 = Line(UP*1.5, DOWN*1.5).shift(RIGHT*0.5)
        dline3 = DashedVMobject(line3).set_color(BLUE_D)
        self.play(ShowCreation(dline3))
        self.wait()
        rec2 = Rectangle(width=1, height=1).set_color(BLUE_D).shift(RIGHT*1.1)
        self.play(FadeOut(dline3))
        self.play(DrawBorderThenFill(rec2))
        self.wait(2)
        self.play(FadeOut(rec2))
        final_list = Text("4")
        self.play(TransformMatchingShapes(list_two, final_list, **kw))
        self.play(final_list.animate.scale(3))
        self.wait()
        self.play(FadeOut(final_list))


        class GraphExample(Scene):
    def construct(self):
        axes = Axes((0, 6), (0, 6))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=3))

        

        parabola = axes.get_graph(lambda x: 0.15 * x**0.35)
        parabola.set_stroke(BLUE)
        self.play(
            # FadeOut(step_graph),
            # FadeOut(step_label),
            ShowCreation(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(0, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(0)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(6), run_time=5)
        # self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
