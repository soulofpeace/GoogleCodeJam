package D;

import java.io.File;
import java.io.PrintWriter;
import java.util.*;

public class Main {
	class Point{
		double x , y;
		Point(double x , double y){
			this.x = x;
			this.y = y;
		}
		double dist(Point p){
			return Math.hypot(x - p.x, y - p.y);
		}
	}
	class Item{
		int index;
		int price;
		Item(int i , int p){
			index = i;
			price = p;
		}
	}
	class Store{		
		Point pos;
		List<Item> item;
		Store(Point p , List<Item> i){
			pos = p;
			item = i;
		}
		int size(){
			return item.size();
		}
	}
	int numItem;
	int numStore;
	double priceGus;
	boolean[] perish;
	Store stores[];
	Main(Scanner sc){
		numItem = sc.nextInt();
		numStore = sc.nextInt();
		priceGus = sc.nextDouble();
		perish = new boolean[numItem];
		List<String> itemName = new ArrayList<String>();
		for(int j = 0 ; j < numItem ; j++){
			String item = sc.next();
			if(item.endsWith("!")){
				perish[j] = true;
				item = item.substring(0, item.length() - 1);
			}		
			itemName.add(item);
		}
		stores = new Store[numStore + 1];
		stores[0] = new Store(new Point(0,0) , new ArrayList<Item>());
		for(int j = 1 ;j <= numStore; j++){
			double x = sc.nextDouble();
			double y = sc.nextDouble();
			Point pos = new Point(x , y);
			String line = sc.nextLine();
			Scanner sc2 = new Scanner(line);
			List<Item> list = new ArrayList<Item>();
			while(sc2.hasNext()){
				String arr[] = sc2.next().split(":");
				int index = itemName.indexOf(arr[0]);
				int value = Integer.parseInt(arr[1]);
				Item i = new Item(index , value);
				list.add(i);
			}
			stores[j] = new Store(pos , list);
		}
	}
	class State implements Comparable<State>{
		int item;
		int pos;
		double value;
		State(int i , int p , double v){
			item = i;
			pos = p;
			value = v;
		}
		@Override
		public int compareTo(State o) {
			return Double.compare(value, o.value);
		}
	}
	double solve(){
		double memo[][] = new double[1 << numItem][numStore + 1];
		for(int i = 0 ; i < memo.length ; i++){
			Arrays.fill(memo[i], Double.MAX_VALUE);
		}
		memo[0][0] = 0.0;
		PriorityQueue<State> q = new PriorityQueue<State>();
		q.add(new State(0 , 0 , 0.0));
		while(!q.isEmpty()){
			State cp = q.poll();
			if(cp.item == (1 << numItem) -1 && cp.pos == 0)
				return cp.value;
			for(int i = 0 ; i <= numStore ; i++){
				if(i == cp.pos)continue;
				Store store = stores[i];
				double dist = stores[cp.pos].pos.dist(store.pos);
				int forbid = 0;
				for(int j = 0 ; j < store.size() ; j++){
					Item it = store.item.get(j);
					if(((1 << it.index) & cp.item) != 0){
						forbid |= 1<<j;
					}
				}
				int all = 1 << store.size();
				for(int j = 0 ; j < all ; j++){
					if((j & forbid) != 0)continue;
					int sum = 0;
					boolean f = false;
					int ni = cp.item;
					for(int k = 0 ; k < store.size() ; k++){
						if((j &(1<<k)) != 0){
							Item it = store.item.get(k);
							f |= perish[it.index];
							sum += it.price;
							ni |= 1 << it.index;
						}
					}
					double nv = cp.value + dist * priceGus + sum;
					int np = f ? 0 : i;
					if(f){
						nv += priceGus * stores[0].pos.dist(store.pos);
					}
					if(memo[ni][np] > nv){
						memo[ni][np] = nv;
						q.add(new State(ni , np , nv));
					}
				}
			}
		}
		return -1;
	}
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(new File("D-small.in"));
		int N = sc.nextInt();
		PrintWriter out = new PrintWriter("D.out");
		for(int i = 1 ; i <= N ; i++){
			Main m = new Main(sc);
			out.printf("Case #%d: %.7f\n" ,i , m.solve());
			out.flush();
		}
		out.close();
	}
}
