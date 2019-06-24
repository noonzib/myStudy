package game.slime;

import javax.swing.*;

public class Study01 {
    public static void main(String[] args) {
        //프레임 생성
        JFrame frm = new JFrame("슬라임 퇴치하기");

        //프레임 크기 설정
        frm.setSize(350,350);

        //프레임을 화면 가운데에 배치
        frm.setLocationRelativeTo(null);

        //프레임을 닫았을 때 메모리에서 제거되도록 설정
        frm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 버튼 생성
        JButton btn1 = new JButton("슬라삐");

        // 프레임에다가 버튼 추가
        frm.add(btn1);

        //프레임이 보이도록 설정
        frm.setVisible(true);
    }
}
