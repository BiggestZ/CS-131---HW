import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

public class Circle extends GraphicsObject{
    int width;
    int height;
    Color color;

    public Circle (int x, int y, int width, int height, Color color) {
        super(x,y);
        this.width = width;
        this.height = height;
        this.color = color;
    }
    
    public void draw(Graphics g) {
        g.setColor(this.color);
        g.fillOval(this.x, this.y, this.width, this.height);
    }

    public void update(int pic_width, int pic_height, int frame) {
        if (this.x < 0 || this.x + this.width > pic_width) {
            this.speed_x = -this.speed_x;
        }
        if (this.y < 0 || this.y + this.height > pic_height) {
            this.speed_y = -this.speed_y;
        }
        Random randy = new Random();
        this.color = new Color(randy.nextInt(255),randy.nextInt(255),randy.nextInt(255));
        super.update(pic_width, pic_height, frame);
    } 
}
