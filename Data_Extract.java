 


import java.io.PrintWriter;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import twitter4j.GeoLocation;
import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.conf.ConfigurationBuilder;

public class test1
{
  public static void main(String[] args) throws Exception 
  {
	  File f = new File("Debbie2-Phase2.txt");
	  	        FileOutputStream fos = new FileOutputStream(f);
	  	        PrintWriter pw = new PrintWriter(fos);
     
    ConfigurationBuilder cb = new ConfigurationBuilder();
    cb.setDebugEnabled(true)
      .setOAuthConsumerKey("**************")
      .setOAuthConsumerSecret("*********************")
      .setOAuthAccessToken("************************")
      .setOAuthAccessTokenSecret("***********************");
    Twitter twitter = new TwitterFactory(cb.build()).getInstance();
    //Query query = new Query("tornado");
    double lat;
    double lon;
    double res;
    String resUnit;
    lon = 148.579746;
    lat = -20.401418;
    res = 1000;
    resUnit="km";
    Query query = new Query("CycloneDebbie").geoCode(new GeoLocation(lat,lon), res, resUnit);
    query.since("2017-03-28");
    query.until("2017-03-29");
    int numberOfTweets = 1300;
    long lastID = Long.MAX_VALUE;
    int cnt=0;
    ArrayList<Status> tweets = new ArrayList<Status>();
    while (tweets.size () < numberOfTweets) {
      if (numberOfTweets - tweets.size() > 50)
        query.setCount(50);
      else 
        query.setCount(numberOfTweets - tweets.size());
      try {
        QueryResult result = twitter.search(query);
        tweets.addAll(result.getTweets());
      
        for (Status t: tweets) 
          if(t.getId() < lastID) 
              lastID = t.getId();

      }

      catch (TwitterException te) {
        System.out.println("Couldn't connect: " + te);
      }; 
      query.setMaxId(lastID-1);
    }

    for (int i = 0; i < tweets.size(); i++) {
    	
      Status t = (Status) tweets.get(i);
      String a="Found : " + i +"\n\n";
      System.out.println(a);
      if(t.getGeoLocation()!= null)
      {
    	  
      
    	  GeoLocation loc=t.getGeoLocation();

      String user = t.getUser().getScreenName();
      String msg = t.getText();
      
      String myLon = Double.toString(loc.getLongitude());
      String myLat = Double.toString(loc.getLatitude());  
     
       String src=("\n\n#################################################\n#$%%$# " + i + " USER: " + user + " wrote: " + msg + " @Oshy@ Time: " + t.getCreatedAt().toString() + " " + myLon + " " + myLat + "\n\n");
       System.out.println(src);
       pw.write(src);
       cnt++; 
     
      } 
      
      else
      {

          String user = t.getUser().getScreenName();
          String msg = t.getText();
           
         
           String src=("#$%%$# " + i + " USER: " + user + " wrote: " + msg + " @Oshy@ Time: " + t.getCreatedAt().toString() + " -1 -1" + "\n\n");
           System.out.println(src);
           pw.write(src);
      }
    }
    String cnts = Integer.toString(cnt);
    System.out.println(cnts);
    pw.flush();
       fos.close();
      pw.close();
      
   
    }
  }
  

