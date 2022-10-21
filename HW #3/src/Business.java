public class Business {

	// Member Vars

	public String formalName;
	public String informalName;
	public String startDate;
	public double latitude;
	public double longitude;
	
	
	
	// Full Constructor

	public Business(String formalName, String informalName, String startDate,
					double latitude, double longitude) {
		this.formalName = formalName;
		this.informalName = informalName;
		this.startDate = startDate;

		if (latitude > 90 || latitude < -90){
			this.latitude = 0.0;
		} else {
			this.latitude = latitude;
		}

		if (longitude > 180 || longitude < -180){
			this.longitude = 0.0;
		} else {
			this.longitude = longitude;
		}
	}

	//Partial Constructor

	public Business(String formalName, String informalName, String startDate) {
		this.formalName = formalName;
		this.informalName = informalName;
		this.startDate = startDate;
	}

	//Gets name of business

	public String getName() {
		if (this.informalName.isEmpty()) {
			return this.formalName;
		} else {
			return this.informalName;
			}
		}

	// Gets Latitude

	public double getLatitude() {
		return this.latitude; // FIXME delete when ready
	}

	// Sets Latitude

	public boolean setLatitude(double latitude) {
		if ( latitude >= -90 && latitude <= 90 ){
			this.latitude = latitude;
			return true; // Return true if latitude is changed
		} else {
			return false; // False if no change
		}
	}

	// Gets Longitude

	public double getLongitude() {
		return this.longitude; // FIXME delete when ready
	}

	// Sets Longitude

	public boolean setLongitude(double longitude) {
		if ( longitude >= -180 && longitude <= 180 ){
			this.longitude = longitude;
			return true; // True if longitude changes
		} else {
			return false; // False if no change
		}
	}

	// Gets the Day

	public int getStartDay() {
		return Integer.parseInt(this.startDate.substring(3,5)); // FIXME delete when ready
	}

	// Gets the Month

	public int getStartMonth() {
		return Integer.parseInt(this.startDate.substring(0,2));
	}

	// Gets the Year

	public int getStartYear() {
		return Integer.parseInt(this.startDate.substring(6)); // FIXME delete when ready
	}
}