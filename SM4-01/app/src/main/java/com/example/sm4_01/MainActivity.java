package com.example.sm4_01;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button tBtn, dBtn, eBtn, cBtn;
    AlertDialog alertDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tBtn = findViewById(R.id.tBtn);
        dBtn = findViewById(R.id.dBtn);
        eBtn = findViewById(R.id.eBtn);
        cBtn = findViewById(R.id.cBtn);

        tBtn.setOnClickListener(this);
        dBtn.setOnClickListener(this);
        eBtn.setOnClickListener(this);
        cBtn.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        if(v == tBtn) {
            //토스트 메시지 출력하기
            Toast.makeText(getApplicationContext(), "스앱 수행평가입니다.", Toast.LENGTH_SHORT).show();
        }
        else if(v == dBtn) {
            //대화상자 띄우기
            AlertDialog.Builder builder = new AlertDialog.Builder(this);
            builder.setIcon(android.R.drawable.ic_dialog_alert);
            builder.setTitle("알림");
            builder.setMessage("정말 종료하시겠습니까?");
            builder.setPositiveButton("네", null);
            builder.setNegativeButton("아니요", null);

            alertDialog = builder.create();
            alertDialog.show();
        }
        else if(v == eBtn) {
            //웹브라우저 띄우기
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://y-y.hs.kr"));
            startActivity(intent);
        }
        else  if(v == cBtn) {
            //계산기 화면(MainActivity2.java)으로 이동
            Intent intent = new Intent(this, MainActivity2.class);
            startActivity(intent);
        }
    }
}
