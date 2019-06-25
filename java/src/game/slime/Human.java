// Human.java

package game.slime;

class Human {

    String name;
    int hp = 100;

    public Human(String n) {
        name = n;
    }

    public void attack(Slime s) {

        s.hp = s.hp - 30;

        if (s.hp < 1) {
            Study01.lbl.setText(s.name + "는 사망했다\n");
            Study01.lbl2.setText("");
        } else {
            Study01.lbl.setText("현재 " + s.name + "의 체력은 " + s.hp + "이다\n");
        }

    }

}
