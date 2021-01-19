package jungol;

import java.util.HashMap;
import java.util.Scanner;

public class HashMapEX {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashMap<Character, Integer> map = new HashMap<>();
		
		map.put('a', 0);
		map.put('b', 0);
		map.put('c', 0);
		
		for(char c : map.keySet()) {
			System.out.printf("%c %d", c, map.get(c));
			System.out.println();
		}
		System.out.println(map.getOrDefault('a', 4));
		System.out.println(map.getOrDefault('z', 4));
		for (char c : map.keySet() ) {
			System.out.printf("%c %d\n", c, map.get(c));
		}
		
		System.out.println();
		System.out.println(map.putIfAbsent('a', 3));
		System.out.println(map.putIfAbsent('z', 3));
		for (char c : map.keySet() ) {
			System.out.printf("%c %d\n", c, map.get(c));
		}
		
		System.out.println("-------------");
		System.out.println(map.computeIfPresent('a', (k, v) -> ++v));
		System.out.println(map.computeIfPresent('f', (k, v) -> ++v));
		
		for (char c : map.keySet() ) {
			System.out.printf("%c %d\n", c, map.get(c));
		}
	}

}
