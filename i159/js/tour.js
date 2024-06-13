AFRAME.registerComponent("tour", {
    schema : {
        state : {
            type : "string",
            default : "places-list"
        },
        selectedCard : {
            type: "string",
            default: "#card1"
        }
    },

    init: function() {
        this.placesContainer = this.el;

        this.createCards();
    },

    tick: function () {
        const { state } = this.el.getAttribute("tour");

        if (state === "view"){
            this.hideEl([this.placesContainer]);
            this.showView();
        }
    },

    hideEl: function (elList) {
        elList.map((el)=>{
            el.setAttribute("visible", false);
        });
    },

    showView: function(){
        const { selectedCard } = this.data;
        const skyEl = document.querySelector("#main-container");
        skyEl.setAttribute("material", {
            src: `./assets/360_images/${selectedCard}/place-0.jpg`,
            color: "#fff"
        })
    },

    createCards: function() {
        const thumbNailsRef = [
            {
                id: "taj-mahal",
                title: "Taj Majal",
                url: "./assets/thumbnails/taj_mahal.png"
            },
            {
                id:"budapest",
                title:"Budapest",
                url: "./assets/thumbnails/budapest.jpg"
            },
            {
                id:"eiffel-tower",
                title: "Torre Eiffel",
                url: "./assets/thumbnails/eiffel_tower.jpg"
            },
            {
                id: "new-york-city",
                title: "Nueva York",
                url: "./assets/thumbnails/new_york_city.png"
            },
        ]

        let prevoiusXPosition = -60;

        for(var item of thumbNailsRef) {
            const posX = prevoiusXPosition + 25;
            const posY = 10;
            const posZ = -40;
            const position = {x: posX, y: posY, z: posZ}

            prevoiusXPosition = posX;

            const borderEl = this.createBorder(position, item.id);
            const thumbNail = this.createThumbnail(item);
            const titleEl = this.createTitleEl(position, item);

            borderEl.appendChild(thumbNail);
            borderEl.appendChild(titleEl);

            this.placesContainer.appendChild(borderEl);
        }
    },

    createBorder: function(position, id){
        const entityEl = document.createElement("a-entity");
        entityEl.setAttribute("id", id);
        entityEl.setAttribute("visible", true);
        entityEl.setAttribute("geometry", {
            primitive: "ring",
            radiusInner: 9,
            radiusOuter: 10
        });
        entityEl.setAttribute("position", position);
        entityEl.setAttribute("material", {
            color:"#00bcd4",
            opacity: 0.4
        });

        entityEl.setAttribute("cursor-listener",{})
        return entityEl;
    },

    createThumbnail: function(item){
        const entityEl = document.createElement("a-entity");
        entityEl.setAttribute("visible", true);
        entityEl.setAttribute("geometry", {
            primitive: "circle",
            radius: 9
        });
        entityEl.setAttribute("material", {
            src: item.url
        });

        return entityEl;
    }, 
    
    createTitleEl: function(position, item){
        const entityEl = document.createElement("a-entity");
        entityEl.setAttribute("text", {
            font: "exo2bold",
            align: "center",
            width: 60,
            color: "#e65100",
            value: item.title
        });
        const elPosition = position;
        elPosition.y = -20;
        entityEl.setAttribute("position", elPosition);
        entityEl.setAttribute("visible", true);

        return entityEl;
    },



});
