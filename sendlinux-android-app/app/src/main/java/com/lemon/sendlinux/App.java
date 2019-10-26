package com.lemon.sendlinux;

import android.annotation.SuppressLint;
import android.app.Application;
import android.content.Context;
import android.provider.Settings;

@SuppressLint("StaticFieldLeak")
public class App extends Application {

    private static Context context;
    private static String UUID;

    @SuppressLint("HardwareIds")
    public void onCreate() {
        super.onCreate();
        App.context = getApplicationContext();
        UUID = Settings.Secure.getString(getContentResolver(), Settings.Secure.ANDROID_ID);
    }

    public static Context getAppContext() {
        return App.context;
    }

    public static String getUUID() {
        return App.UUID;
    }
}
