from flask.views import MethodView
from imports.main import *
from models.publication import Publication

security = [{"BearerAuth": []}]
security = []

@publications.route('/')
class PublicationsAPI(MethodView):
    @publications.doc(description="Get all publications", security=security) 
    @publications.arguments(UserListQuery, location="query")
    @publications.response(200, schema=PublicationListQuery)
    @jwt_required()
    def get(self, args):
        order_by = args.get("order_by", PublicationOrderByEnum.created_at)
        order = args.get("order", PublicationOrderEnum.asc)
        limit = args.get("limit")
        start = args.get("start", 0)
        order_by = {
            PublicationOrderByEnum.created_at: Publication.created_at,
            PublicationOrderByEnum.updated_at: Publication.updated_at,
            PublicationOrderByEnum.title: Publication.title,
        }[order_by]
        reverse = order == "desc"
        query = Publication.query.order_by(order_by)
        query = query.offset(start)
        if reverse:
            query = query.reverse()
        if limit is not None:
            query = query.limit(limit)
        publications = query.all()
        return jsonify({"publications": [user.serialize() for user in publications]})

    @publications.doc(description="Create a User")
    @publications.arguments(CreatePublication, location="query")
    @publications.arguments(CreatePublicationImage, location="files")
    @publications.response(201, schema=PublicationResponse)
    @jwt_required()
    def post(self, args, files):

        image = files['image']
        
        name = f"{get_jwt_identity()['username']}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.jpg"
        url = f"/api/images/publications/{name}"
        
        
        merge_images(f"images/publications/{name}", image, args["sticker"], (args['x'], args['y']))
        
        with open(f"images/publications/{name}", "wb") as f:
            f.write(image.read())
        
        args["user"] = User.query.get(get_jwt_identity()["id"])
        args["url"] = url
        
        publication = Publication(**args)
        db.session.add(publication)
        db.session.commit()
        return jsonify({"publication": publication.serialize()})


@publications.route('/<int:id>')
class PublicationsAPI(MethodView):
    @publications.doc(description="Get a user by ID")
    @publications.response(200, schema=PublicationResponse)
    @jwt_required()
    def get(self, id):
        publication = Publication.query.get(id)
        return jsonify(publication.serialize())
    
    @publications.doc(description="Update a user by ID")
    @publications.arguments(UpdatePublication)
    @publications.response(200, schema=PublicationResponse)
    @jwt_required()
    def put(self, args, id):
        publication = Publication.query.get(id)
        publication.update(**args)
        db.session.commit()
        return jsonify(publication.serialize())
    
    @publications.doc(description="Delete a user by ID")
    @publications.response(204)
    @jwt_required()
    def delete(self, id):
        publication = Publication.query.get(id)
        db.session.delete(publication)
        db.session.commit()
        return jsonify({})
    
    