package com.lemon.sendlinux;

import android.content.Intent;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView textView = findViewById(R.id.text);
        String text = "-SendLinux-" + "\n" + "UUID: " + App.getUUID();
        textView.setText(text);
        textView.setTextSize(24);

        checkForData();

    }

     private void checkForData() {
         if(getIntent().getStringExtra(Intent.EXTRA_TEXT) != null) {
             final String intentText = getIntent().getStringExtra(Intent.EXTRA_TEXT);
             if (intentText != null) {
                new SendAsyncTask().execute(intentText.getBytes());
             }
         }
     }
}
