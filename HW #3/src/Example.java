public class Example {
	public static void main(String[] args) {

		Business the_york = new Business("The York Project", "The York", "02/06/2007");

		System.out.println(the_york.getName()); // "The York"
		System.out.println(the_york.getStartDay()); // 6
		System.out.println(the_york.getStartMonth()); // 2
		System.out.println(the_york.getStartYear()); // 2007
		System.out.println(the_york.getLatitude()); // 0.0
		System.out.println(the_york.getLongitude()); // 0.0
		System.out.println(the_york.setLatitude(-100)); // false
		System.out.println(the_york.setLongitude(-200)); // false
		System.out.println(the_york.setLatitude(34.1213)); // true
		System.out.println(the_york.setLongitude(-118.2062)); // true
		System.out.println(the_york.getLatitude()); // 34.1213
		System.out.println(the_york.getLongitude()); // -118.2062

		Business zweet = new Business("Zweet Cafe Inc", "", "09/30/2015", 34.1295, -118.2168);

		System.out.println(zweet.getName()); // "Zweet Cafe Inc"
		System.out.println(zweet.getStartDay()); // 30
		System.out.println(zweet.getStartMonth()); // 9
		System.out.println(zweet.getStartYear()); // 2015
		System.out.println(zweet.getLatitude()); // 34.1295
		System.out.println(zweet.getLongitude()); // -118.2168

	}
}
