
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script>

      var types = [
                      
                      "atm",
                      
                      "bank",
                     
                      "cafe",
                      
                      "clothing_store",
                      
                      
                      "gym",
                      
                      "hospital",
                      
                      "library",
                      
                      
                      "park",
                      
                      "restaurant",
                      
                      "shopping_mall",
                      
                      "store",
                      
                      "train_station",
                    
                    ];


      function distance(a,b){
          var length=((a[0]-b[0])*(a[0]-b[0]))+(a[1]-b[1])*(a[1]-b[1]);
          return length;
      }

      var nearest = 10000000;
      var thisPlaceX=0,thisPlaceY=0;
      var thisPlaceType = "";
      var myPlace = [];

      function getNearbyPlaces(latitude,longitude,type,index){
        var url = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location="
            +latitude+","+longitude+"&radius=500&type="+type+"&key=AIzaSyDLSlQykTgmoe5ukRxrW6AAPA-42xp3hPA";

            
      
        $(document).ready(function(){
          
          $.getJSON(url,function(data){
            console.log("inside ",index);

            for (var i = 0; i < data.results.length; i++) {
              var x = latitude-data.results[i].geometry.location.lat;
              var y = longitude-data.results[i].geometry.location.lng;
              
              if(myPlace[index][2]>x*x+y*y){
                myPlace[index][2] = x*x+y*y;
                thisPlaceX = data.results[i].geometry.location.lat;
                thisPlaceY = data.results[i].geometry.location.lng;
                thisPlaceType = type;
                myPlace[index] = [thisPlaceX,thisPlaceY,myPlace[index][2],type];
                
              }
            }

            // console.log(index,thisPlaceX,thisPlaceY,myPlace[index][2],thisPlaceType);
            
          });

        });
      }


      function getPlaceType(latitude,longitude,index,data){
        
        for(var type = 0; type<types.length; type++){
          getNearbyPlaces(latitude,longitude,types[type],index);
        }
        
      }

      function f1(response){
        var data = response[0];
        var i = response[1];
        var myLatLng = {lat: data.locations[i].latitudeE7, lng: data.locations[i].longitudeE7};
        getPlaceType(myLatLng.lat/10000000,myLatLng.lng/10000000,response[1],response[0]);
        return [response[0],response[1]+1]; 
      }


      function main(){
        
        $.getJSON('data.json',function(data){
          console.log(data);

          


          for (var i = 0; i < 10; i++) {
            myPlace[i] = [0,0,100000000,""];
            
            
          }
          
          
          var promise = new Promise(function(resolve,reject){
            resolve([data,0]);
          });

          promise.then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(f1).then(function(response){
            console.log("hello ",response);
          });
            
            window.setTimeout(function(){
              for (var i = 0; i < 10; i++) {
                console.log(i,myPlace[i]);
              }
              

            }, 10000);

            
        });
        
      }

      main();
      
    </script>
  </head>
  <body></body>
</html>