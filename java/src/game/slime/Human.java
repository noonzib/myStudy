// Human.java

package game.slime;

import javax.swing.*;
import java.util.Timer;
import java.util.TimerTask;

class Human {

    String name;
    int hp = 100;

    public Human(String n) {
        name = n;
    }

    public void attack(Slime s) {
        ImageIcon bsImg_fire = new ImageIcon(Study01.class.getResource("/game/slime/img/slime2(blue).png"));
        ImageIcon rsImg_fire = new ImageIcon(Study01.class.getResource("/game/slime/img/slime2(red).png"));

        if(s == Study01.bs1){
            Study01.imgLbl.setIcon(bsImg_fire);
        } else {
            Study01.imgLbl2.setIcon(rsImg_fire);
        }

        Timer timer1 = new Timer();
        TimerTask task1 = new TimerTask() {
            @Override
            public void run() {
                Study01.imgLbl.setIcon(Study01.bsImg);
                Study01.imgLbl2.setIcon(Study01.rsImg);
                timer1.cancel();
            }
        };

        timer1.schedule(task1,500);

        s.hp = s.hp - 30;

        if (s.hp < 1) {
            if(s == Study01.bs1){
                Study01.btn1.setEnabled(false);
            } else {
                Study01.btn2.setEnabled(false);
            }
            Study01.lbl.setText(s.name + "는 사망했다\n");
            Study01.lbl2.setText("");
        } else {
            Study01.lbl.setText("현재 " + s.name + "의 체력은 " + s.hp + "이다\n");
        }

    }

}
