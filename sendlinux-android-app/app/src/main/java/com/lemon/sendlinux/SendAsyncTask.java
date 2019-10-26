package com.lemon.sendlinux;

import android.os.AsyncTask;

public class SendAsyncTask extends AsyncTask<byte[], Void, String> {
    @Override
    protected String doInBackground(byte[]... params) {
        new MqttHelper().send(params[0], App.getUUID());
        return "Sent!";
    }

    @Override
    protected void onPostExecute(String result) {
    }
}
