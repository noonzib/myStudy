package com.noonzib.calculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    Button btn1;
    Button btn2;
    Button btn3,btn4,btn5,btn6,btn7,btn8,btn9;
    Button btnAC, btnPlus,btnMins, btnMultiply, btnDiv,btnEqual;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn1 = (Button)findViewById(R.id.btn1);
        btn2 = (Button)findViewById(R.id.btn2);
        btn3 = (Button)findViewById(R.id.btn3);
        btn4 = (Button)findViewById(R.id.btn4);
        btn5 = (Button)findViewById(R.id.btn5);
        btn6 = (Button)findViewById(R.id.btn6);
        btn7 = (Button)findViewById(R.id.btn7);
        btn8 = (Button)findViewById(R.id.btn8);
        btn9 = (Button)findViewById(R.id.btn9);
        btnAC = (Button)findViewById(R.id.btnAC);
        btnPlus = (Button)findViewById(R.id.btnPlus);
        btnMins = (Button)findViewById(R.id.btnMins);
        btnMultiply = (Button)findViewById(R.id.btnMultiply);
        btnDiv = (Button)findViewById(R.id.btnDiv);
        btnEqual = (Button)findViewById(R.id.btnEqual);
    }
}
