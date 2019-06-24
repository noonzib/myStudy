package game.shooting;

import javax.swing.*;
import java.awt.*;

public class game {
    public static void main(String[] args) {
        game_Frame fms = new game_Frame();
    }
}

class game_Frame extends JFrame{
    int f_width = 800;
    int f_height = 600;

    Toolkit tk = Toolkit.getDefaultToolkit();
    Image me_img = tk.getImage("/airplane.png");

    game_Frame(){
        init();
        start();
        setTitle("슈팅 게임 만들기");
        setSize(f_width,f_height);
        Dimension screen = tk.getScreenSize();

        int f_xpos=(int)(screen.getWidth()/2 - (f_width/2));
        int f_ypos=(int)(screen.getHeight()/2 - (f_height/2));

        setLocation(f_xpos,f_ypos);
        setResizable(false);
        setVisible(true);
    }
    public void init(){

    }
    public void start(){
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    public void paint(Graphics g){
        g.clearRect(0,0,f_width,f_height);
        g.drawImage(me_img, 100, 100, this);
    }
}
