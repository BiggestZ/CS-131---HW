
import java.util.ArrayList;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Animation extends JPanel {
    private int framesPerSecond = 25;
    private int msPerFrame = 1000 / framesPerSecond;

    private int canvasWidth;
    private int canvasHeight;
    private Color backgroundColor;

    private ArrayList<GraphicsObject> objects;

    public Animation(int width, int height) {
        this(width, height, Color.WHITE);
    }

    public Animation(int width, int height, Color color) {
        this.canvasWidth = width;
        this.canvasHeight = height;
        this.backgroundColor = color;
        this.objects = new ArrayList<GraphicsObject>();
    }

    public void showCanvas() {
        JFrame frame = new JFrame("Animation");
        frame.getContentPane().add(this, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Dimension dim = new Dimension(this.canvasWidth, this.canvasHeight);
        frame.getContentPane().setPreferredSize(dim);
        frame.pack();
        frame.setVisible(true);
    }

    public void paint() {
        this.paint(this.getGraphics());
    }

    @Override
    public void paint(Graphics g) {
        Color oldColor = g.getColor();
        g.setColor(this.backgroundColor);
        g.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
        g.setColor(oldColor);

        for (GraphicsObject obj : this.objects) {
            obj.draw(g);
        }
    }

    public void update(int frame) {
        for (GraphicsObject obj : this.objects) {
            obj.update(this.canvasWidth, this.canvasHeight, frame);
        }
    }

    public void addObject(GraphicsObject obj) {
        this.objects.add(obj);
    }

    public void start()
            throws InterruptedException {
        this.showCanvas();
        Thread.sleep(500);
        int frame = 0;
        while (true) {
            this.update(frame);
            this.paint();
            Thread.sleep(this.msPerFrame);
            frame++;
        }
    }

    public static void main(String[] args)
            throws InterruptedException {
        int PICTURE_WIDTH = 560;
        int PICTURE_HEIGHT = 560;

        Animation pic = new Animation(PICTURE_WIDTH, PICTURE_HEIGHT, Color.WHITE);

        Rectangle Bergie = new Rectangle(0, 160, 50, 50, new Color(154, 8, 178));
        Bergie.speed_x = 5;
        pic.addObject(Bergie);

        Rectangle bigz = new Rectangle(300, 0, 75, 75, Color.ORANGE);
        bigz.speed_x = -2;
        pic.addObject(bigz);

        Circle fred = new Circle (400, 120, 75,75, Color.WHITE);
        fred.speed_x = -5;
        fred.speed_y = 5;
        pic.addObject(fred);

        pic.start();
    }

}