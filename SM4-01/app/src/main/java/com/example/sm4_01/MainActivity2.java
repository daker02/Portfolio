package com.example.sm4_01;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity2 extends AppCompatActivity implements View.OnClickListener {

    EditText fn, sn;
    Button plus, minus, mul, div;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        fn = findViewById(R.id.fn);
        sn = findViewById(R.id.sn);

        plus = findViewById(R.id.plus);
        minus = findViewById(R.id.minus);
        mul = findViewById(R.id.mul);
        div = findViewById(R.id.div);

        fn.setOnClickListener(this);
        sn.setOnClickListener(this);

        plus.setOnClickListener(this);
        minus.setOnClickListener(this);
        mul.setOnClickListener(this);
        div.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        int a = Integer.parseInt(fn.getText().toString());
        int b = Integer.parseInt(sn.getText().toString());
        int c = 0;

        if(v == plus) {
            c = a + b;
        }
        else if(v == minus) {
            c = a - b;
        }
        else  if(v == mul) {
            c = a * b;
        }
        else if (v == div) {
            c = a / b;
        }
        Toast.makeText(getApplicationContext(), "결과는: " + c + "입니다", Toast.LENGTH_SHORT).show();
    }
}
