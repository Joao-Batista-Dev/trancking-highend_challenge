from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from countries.models import Assessment
from countries.serializers import AssessmentSerializer
from countries.countries_api import get_countries_all, get_countrie_by_name

class GetTopCountriesApiViews(APIView):
    def get(self, request):
        countries = get_countries_all()

        get_top_10 = sorted(
            countries,
            key=lambda x: x["populacao"], 
            reverse=True
        )[:10]

        return Response(get_top_10)


class GetCountriesApiViews(APIView):
    def get(self, request):
        name = request.GET.get("name")
        if not name:
            return Response({"erro": "Informe o parâmetro ?name="}, status=status.HTTP_400_BAD_REQUEST)

        countrie = get_countrie_by_name(name)  
        if not countrie:
            return Response({"erro": "País não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        country_name = countrie["name"]["common"]
        assessment = Assessment.objects.filter(countrie=country_name)

        countrie["curtidas"] = assessment.filter(liked=True).count()
        countrie["nao_curtidas"] = assessment.filter(liked=False).count()

        return Response(countrie)


class PostCountriesLikedApiViews(APIView):
    def post(self, request):
        countrie = request.data.get('countrie')
        liked = request.data.get('liked')

        if countrie is None or liked is None:
            return Response({
                "error": "Verifique se os dados estão corretos!",
            }, status=status.HTTP_400_BAD_REQUEST)
        
        assessment = Assessment.objects.create(countrie=countrie, liked=liked)

        total_likes = Assessment.objects.filter(countrie=countrie).count()
        likes = Assessment.objects.filter(countrie=countrie, liked=True).count()
        not_lkes = Assessment.objects.filter(countrie=countrie, liked=False).count()

        return Response({
            "countrie": countrie,
            "status": "sucesso",
            "total_likes": total_likes,
            "likes": likes,
            "not_likes": not_lkes
        }, status=status.HTTP_201_CREATED)






