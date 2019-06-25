package game.slime;

import javax.swing.*;
import javax.swing.plaf.FontUIResource;
import java.awt.*;
import java.util.Enumeration;

public class Study01 {
    //라벨 변수 선언
    static JLabel lbl, lbl2, imgLbl, imgLbl2;
    static ImageIcon bsImg, rsImg;
    static JButton btn1, btn2;
    //슬라임과 인간 객체 생성
    static BlueSlime bs1 = new BlueSlime("슬라삐");
    static RedSlime rs1 = new RedSlime("슬라디");
    static Human h = new Human("알렉스");

    public static void main(String[] args) {

        //모든 글꼴 통일
        Enumeration<Object> keys = UIManager.getDefaults().keys();
        while (keys.hasMoreElements()) {
            Object key = keys.nextElement();
            Object value = UIManager.get(key);
            if(value instanceof FontUIResource)
                UIManager.put(key, new FontUIResource("굴림", Font.PLAIN, 14));
        }
        // [start] 프레임 생성
        JFrame frm = new JFrame();
        frm.setTitle("슬라임 퇴치하기");
        frm.setSize(350,350);
        frm.setLocationRelativeTo(null);
        frm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frm.getContentPane().setLayout(null);
        //[end] 프레임 설정

        //[start] 버튼 설정
        btn1 = new JButton(bs1.name);
        btn2 = new JButton(rs1.name);
        btn1.setBounds(30,170,122,30);
        btn2.setBounds(182,170,122,30);
        frm.getContentPane().add(btn1);
        frm.getContentPane().add(btn2);
        // [end] 버튼 설정

        // 라벨 설정
        lbl = new JLabel();
        lbl.setBounds(30,210,274,50);
        lbl.setText("게임을 시작합니다");
        lbl.setHorizontalAlignment(JLabel.CENTER);
        frm.getContentPane().add(lbl);

        // 라벨2 설정
        lbl2 = new JLabel();
        lbl2.setBounds(30,240, 274, 50);
        lbl2.setText(h.name + "의 체력은 "+h.hp +"입니다.");
        lbl2.setHorizontalAlignment(JLabel.CENTER);
        frm.getContentPane().add(lbl2);

        // [start]이미지라벨 생성
        imgLbl = new JLabel();
        bsImg = new ImageIcon(Study01.class.getResource("/game/slime/img/slime(blue).png"));
        imgLbl.setIcon(bsImg);
        imgLbl.setBounds(30,30,122,130);
        imgLbl.setHorizontalAlignment(JLabel.CENTER);
        frm.getContentPane().add(imgLbl);
        // [end]

        // [start] 이미지 라벨2 생성
        imgLbl2 = new JLabel();
        rsImg = new ImageIcon(Study01.class.getResource("/game/slime/img/slime(red).png"));
        imgLbl2.setIcon(rsImg);
        imgLbl2.setBounds(182,30,122,130);
        imgLbl2.setHorizontalAlignment(JLabel.CENTER);
        frm.getContentPane().add(imgLbl2);
        // [end]

        //프레임이 보이도록 설정
        frm.setVisible(true);

        // 버튼이 눌렸을때
        btn1.addActionListener(event -> {

            battle(bs1);
        });

        btn2.addActionListener(event -> {

            battle(rs1);
        });

    }
    public static void battle(Slime s){
        //슬라임이 살아있을때만 공격
        h.attack(s);

        if(s instanceof BlueSlime){
            ((BlueSlime) s).heal(s);
        }else{
            s.attack(h);
        }
        // 슬라임이 모두 죽으면 게임 클리어
        if(bs1.hp < 1 && rs1.hp < 1){
            JOptionPane.showMessageDialog(lbl2, "Game Clear!");
            System.exit(0);
        }
    }
}
