package com.lemon.sendlinux;

import android.content.Intent;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity implements TaskCallback {

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
                new SendAsyncTask(this).execute(intentText.getBytes());
             }
         }
     }

    @Override
    public void taskDone() {
        Toast.makeText(this, "Sharing done!", Toast.LENGTH_LONG).show();
        finish();
    }

}
