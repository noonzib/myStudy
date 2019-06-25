// Slime.java

package game.slime;

import javax.swing.JOptionPane;

class Slime {

    String name;
    int hp = 80;

    // 생성자
    public Slime(String n) {

        name = n;

    }

    // 공격
    public void attack(Human h){
        attack(h,10);
    }
    public void attack(Human h, int damage) {

        if (hp > 0) {
            h.hp = h.hp - damage;
            if (h.hp < 1) {
                JOptionPane.showMessageDialog(null, "Game Over");
                System.exit(0);
            }

            Study01.lbl2.setText("현재 " + h.name + "의 체력은 " + h.hp + ".");
        }

    }

}

class BlueSlime extends Slime{
    //생성자
    BlueSlime(String n){
        super(n);
    }

    //약한 공격
    @Override
    public void attack(Human h){
        attack(h, 8);
    }

    //치료
    void heal(Slime s){
        if(hp > 0 && s.hp > 0){
            s.hp += 10;

            if(s.hp > 80){
                s.hp = 80;
            }

            Study01.lbl2.setText(name + "는 "+s.name+"를 치료. 그의 체력은 "+s.hp+".");
        }
    }
}
class RedSlime extends Slime{
    RedSlime (String n){
        super(n);
    }

    @Override
    public void attack(Human h){
        attack(h, 15);
    }
}
class BlackSlime {
    String name;
    int hp = 100;
    int str = 30; // 공격력
    int def = 15; // 방어력
    int dex = 10; // 민첩성

    //생성자
    public BlackSlime(String n){
        name = n;
    }

    //공격
    public void attack(Human h){

    }

    //도망
    public void runAway(){

    }

    //이동거리 증가
    public void speedUp(Human h){

    }
}
class YellowSlime {
    String name;
    int hp = 100;
    int str = 30; // 공격력
    int def = 15; // 방어력
    int dex = 10; // 민첩성

    //생성자
    public YellowSlime(String n){
        name = n;
    }

    //공격
    public void attack(Human h){

    }

    //도망
    public void runAway(){

    }

    //화염 공격
    public void defDown(Human h){

    }
}
