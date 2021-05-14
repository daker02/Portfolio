package com.example.sm3_23;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity2 extends AppCompatActivity implements View.OnClickListener {
    Button input;
    Button cancel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        input = findViewById(R.id.input);
        input.setOnClickListener(this);
        cancel = findViewById(R.id.cancelBtn);
        cancel.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        if(view == input) {
            Toast.makeText(this, "입력되었습니다", Toast.LENGTH_SHORT).show();
        }else if(view == cancel) {
            Toast.makeText(this, "취소되었습니다", Toast.LENGTH_SHORT).show();
        }
    }
}