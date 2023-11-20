function main(){
  const { getJson } = require("serpapi");
  const z = document.getElementById("query");
  getJson({
    api_key: "624f19b460aa70e54a309edca59430ace68c658cb4f60fd49981a3d25e2191e0",
    engine: "google",
    q: z,
    google_domain: "google.com",
    gl: "us",
    hl: "en",
    num: "100",
    start: "0"
  }, (json) => {
    document.getElementById(`output`) = json["organic_results"].length + " results found\n";
    let i = 0;
    while (i < Object.keys(json["organic_results"]).length) {
      if (json["organic_results"][i]["link"].search("nytimes") != -1){
        document.createElement("div").appendChild("\"" + json["organic_results"][i]["title"] + "\"");
        document.createElement("div").appendChild(json["organic_results"][i]["link"] + "\n  position: " + i);
      }
    i++;
    }
  });
}
document.getElementById("activate").addEventListener("click", main);